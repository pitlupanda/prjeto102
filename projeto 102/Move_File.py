import os
import shutil

from_dir = "C:/Users/Pedro/OneDrive/Área de Trabalho/aulas de python/aula102/pedro"
to_dir = "C:/Users/Pedro/OneDrive/Área de Trabalho/aulas de python/projeto 102"
list_of_files = os.listdir(from_dir)
print(list_of_files)
for file_name in list_of_files:
    name, extension = os.path.splitext(file_name) #splitext   separa nome e extençao
    #print(name)
    #print(extension)
    if extension == '':
        continue
    if extension in ['.gif', '.png', '.jpeg', '.jpg', '.jfif', '.txt', '.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name #caminho de origem
        path2 = to_dir + '/' + 'pedro' #criando pasta
        path3 = to_dir + '/' + 'pedro' + '/' + file_name #pegar o caminho de destino
        #print("path1", path1)
        #print("path3", path3)
        if os.path.exists(path2): # verifica se o caminho 2 existe
            print('movendo ' + file_name + '...') # se existir ele pega os arquivos das imagens 
            shutil.move(path1, path3) # move do camiho 1 para o caminho 3
        else: # se nao existir
            os.makedirs(path2) # cria o caminho 2 
            print('movendo ' + file_name + '...') # pega os arquivos de imagem 
            shutil.move(path1, path3) # move do 1 para o 3