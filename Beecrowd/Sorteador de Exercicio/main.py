import random
import os
import shutil


def procurar_diretorio(caminho_base, nome_procurado):
    for root, dirs, files in os.walk(caminho_base):  
        if nome_procurado in dirs:
            return True
    return False


def criar_diretorio_com_base(caminho_base, nome_diretorio, caminho_modelo):

    caminho_completo = os.path.join(caminho_base, nome_diretorio)


    os.makedirs(caminho_completo)
    print(f"Diretório '{caminho_completo}' criado com sucesso!")


    if os.path.exists(caminho_modelo):
        for item in os.listdir(caminho_modelo):
            origem_item = os.path.join(caminho_modelo, item)
            destino_item = os.path.join(caminho_completo, item)

            if os.path.isdir(origem_item):
                shutil.copytree(origem_item, destino_item)  
            else:
                shutil.copy2(origem_item, destino_item) 
    else:
        print(f"O caminho do modelo '{caminho_modelo}' não foi encontrado.")


def sortear_numero():
    caminho_base = './Beecrowd/python'  
    caminho_modelo = './Beecrowd/Base'  
    sort = False

    while not sort:
        exercise = random.randint(1000, 3084)  
        nome_diretorio = str(exercise) 
        

        if not procurar_diretorio(caminho_base, nome_diretorio):
            criar_diretorio_com_base(caminho_base, nome_diretorio, caminho_modelo)
            sort = True



sortear_numero()
