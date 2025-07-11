import PyPDF2
import os

mesclador = PyPDF2.PdfMerger()

arquivos = os.listdir("arquivos") #os arquivos salvos nessa variável é o que a pasta/diretório especificado encontrou na os.

for arquivo in arquivos:
    mesclador.append(f'arquivos/{arquivo}') #adicionando ao mesclador cada arquivo dentro da pasta arquivo e explicando onde está localizado o arquivo que o mesclador tem que mesclar à ele.

mesclador.write("Arquivos mesclados.pdf")