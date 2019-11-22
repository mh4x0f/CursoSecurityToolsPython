import os
caminhos = []
arquivos = []
pngs = []
for name in os.listdir("teste"):
	caminhos.append(os.path.join("teste", name))
for arq in caminhos:
	if os.path.isfile(arq):
		arquivos.append(arq)
for arq in arquivos:
	if arq.lower().endswith(".png"):
		pngs.append(arq)

print("caminhos: ",format(caminhos))
print("arquivos encontrados: ",format(arquivos))
print("arquivos do tipo .png: ",format(pngs))
