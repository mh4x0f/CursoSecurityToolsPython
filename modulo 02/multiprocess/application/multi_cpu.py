import requests
import multiprocessing
import time
from lxml import html

maximum_tries = 2
links_unvalid = ["javascript", "png", "jpeg", "jpg", "gif", "deb", "exe"]

session = requests.Session()
session.mount('http://', requests.adapters.HTTPAdapter(max_retries=maximum_tries))

class Consumer(multiprocessing.Process):
    def __init__(self, task_queue, result_queue):
        multiprocessing.Process.__init__(self)
        self.task_queue = task_queue
        self.result_queue = result_queue

    def findLinks(self, endereco):
        print("status : website -> %s find links..." % endereco)
        page = requests.get(endereco)
        webpage = html.fromstring(page.content)
        return webpage.xpath('//a/@href')

    def stop(self):
        self.started = False

    def run(self):
        self.started = True
        proc_name = self.name
        while self.started:
            next_task = self.task_queue.get()
            if next_task is None:
                # Poison pill means shutdown
                print('%s: Exiting' % proc_name)
                self.task_queue.task_done()
                break
            print('%s: %s' % (proc_name, next_task))
            answer = next_task()
            links = self.findLinks(answer)
            print(links)
            for link in links:
                self.result_queue.put(link)
            self.task_queue.task_done()
        return

class Task(object):
    def __init__(self, link):
        self.link = link
    def __call__(self):
        time.sleep(0.1)
        return self.link
    def __str__(self):
        return '%s * %s' % ("task", self.link)




if __name__ == '__main__':
    # Establish communication queues
    tasks = multiprocessing.JoinableQueue()
    results = multiprocessing.Queue()
    
    # Start consumers
    num_consumers = multiprocessing.cpu_count() * 2
    print('Creating %d consumers' % num_consumers)
    consumers = [ Consumer(tasks, results)
                  for i in range(num_consumers) ]
    for w in consumers:
        w.start()
    
    # Enqueue jobs
    websites = ['http://econpy.pythonanywhere.com/ex/001.html', 'http://econpy.pythonanywhere.com/']
    for i in websites:
        tasks.put(Task(i))
    
    # Add a poison pill for each consumer
    for i in range(num_consumers):
        tasks.put(None)

    # Wait for all of the tasks to finish
    tasks.join()
    
    # Start printing results
    while not results.empty():
        result = results.get()
        print('Result:', result)