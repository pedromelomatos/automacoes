import os
from tkinter.filedialog import askdirectory #biblioteca que vai pedir o diretório a ser organizado a partir de um popup

diretorio = askdirectory(title="Selecione a pasta com os arquivos a serem organizados.") #abrindo popup pra um diretório ser selecionado.

arquivos_na_pasta = os.listdir(diretorio)
print(arquivos_na_pasta)

tipos = ["sql", "docx", "pdf"]

for arquivo in arquivos_na_pasta:
    for tipo_de_arquivo in tipos:
        if tipo_de_arquivo in arquivo:
            print(f"{arquivo} é do tipo {tipo_de_arquivo}")
            if not os.path.exists(f"{diretorio}/{tipo_de_arquivo}"): #se não tiver uma pasta pra esse arquivo..
                os.mkdir(f"{diretorio}/{tipo_de_arquivo}") #crie ela
            os.rename(f"{diretorio}/{arquivo}", f"{diretorio}/{tipo_de_arquivo}/{arquivo}") #mudando a localização do arquivo no os com os.rename