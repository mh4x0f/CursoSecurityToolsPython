

import os
import glob
arquivos = []
diretorio_atual = os.getcwd() 
filtro = "*.*"

for dir, _ , _ in os.walk(diretorio_atual + "/test"):
    arquivos.extend(glob.glob(os.path.join(dir, filtro)))

print(arquivos)
print(len(arquivos))

