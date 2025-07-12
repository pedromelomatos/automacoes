import os
from tkinter.filedialog import askdirectory #biblioteca que vai pedir o diretório a ser organizado a partir de um popup

diretorio = askdirectory(title="Selecione a pasta com os arquivos a serem organizados.") #abrindo popup pra um diretório ser selecionado.

arquivos_na_pasta = os.listdir(diretorio)
print(arquivos_na_pasta)
