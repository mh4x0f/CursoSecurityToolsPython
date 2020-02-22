from termcolor import colored, cprint
import sys 
text = colored('Hello, World!', 'red', attrs=['reverse', 'blink']) 
print(text) 
cprint('Hello, World!', 'green', 'on_red')   
for i in range(10): 
    cprint(i, 'magenta', end=' ') 
cprint("Attention!",'red', attrs=['bold'], file=sys.stdout) 
