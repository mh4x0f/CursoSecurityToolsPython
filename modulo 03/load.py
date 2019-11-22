import os
caminhos = []
arquivos = []
pngs = []
for name in os.listdir(“pasta”):
	caminhos.append(os.path.join(pasta, nome))
for arq in caminhos:
	if os.path.isfile(arq):
		arquivos.append(arq)
for arq in arquivos:
	if arq.lower().endswith(".jpg"):
		pngs.append(arq)
