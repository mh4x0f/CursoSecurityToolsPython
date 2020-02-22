import argparse# importando o modulo 
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--local",dest="env", required=True,help="configura a variavel local") 
parser.add_argument("-u", "--url",dest="url",help="configura a url alvo")   
args = parser.parse_args()

if (args.env):
    print("o user digitou env : {}".format(args.env))
if (args.url):
    print("o alvo foi setado : {} ".format(args.url))
print(args)
