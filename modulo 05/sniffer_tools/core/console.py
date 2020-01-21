import cmd
import sys
from tabulate import tabulate
from core.sniff import Sniffer
import os
from threading import Thread

class Console(cmd.Cmd):
    def __init__(self, parser):
        super(Console, self).__init__()
        self.prompt = "[snifferTools]> "
        self.sniffer = Sniffer(parser)

    def default(self, line):
        os.system(line)
    
    def do_exit(self, line):
        """ comando para sair do sistema """
        sys.exit(0)

    def do_plugins(self, line):
        """ mostra todos os plugins disponiveis""" 
        headers , data = ['Name', 'Status' ] , []
        for plugin in self.sniffer.config.getAllPlugins():
            data.append([plugin , self.sniffer.config.getPluginStatus(plugin)])
        print("Plugins dispinveis:")
        print(tabulate(data, headers, tablefmt="grid"))

    def do_set(self, line):
        args = line.split()
        if (len(args) == 2 and args[0] in self.sniffer.config.getAllPlugins()):
            if (args[1].lower() in ("yes", "true", "t" , "1")):
                self.sniffer.config.setPluginStatus(args[0], True)
                print("[*] {} status : {}".format(args[0],"Ativo"))
            else:
                self.sniffer.config.setPluginStatus(args[0], False)
                print("[*] {} status : {}".format(args[0],"Desativado"))
            return
        elif (len(args) == 2 and args[0] == "filter"):
            self.sniffer.setStringfilter(args[1])
        elif (len(args) == 2 and args[0] == "interface"):
            self.sniffer.setInterface(args[1])

    def do_run(self, line):
        """ inicia sniffer de pacotes """ 
        sniff = Thread(target=self.sniffer.run,  args=())
        sniff.deamon = True
        sniff.start()

    def do_stop(self, line):
        """ para sniffer de pacotes """ 
        self.sniffer.stop()

    def emptyline(self):
        pass