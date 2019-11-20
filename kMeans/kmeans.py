from random import randint
from math import sqrt

#variaveis globais
QTD_COLUNAS = 0

def abrirArquivo(nomeArquivo):
    arquivo = open("../datasets/" + nomeArquivo + ".txt", "r")
    return arquivo

def lerArquivo(nomeArquivo): 
    arquivo = abrirArquivo(nomeArquivo)
    dados = []
    
    labels = arquivo.readline().split()
    global QTD_COLUNAS
    QTD_COLUNAS = len(labels) - 1

    for linha in arquivo:
        obj = linha.split()
        for i in range(1, QTD_COLUNAS+1):
            obj[i] = float(obj[i])
        dados.append(obj)

    return dados

def inicializarClusters(dados):
    cluster_list = []
    valores = []

    for i in range(0, nClusters):       # inicializa uma lista de dicionarios
        flag = 1

        cluster_list.append({ 
            "centroide": [],
            "objs": []
        })

        #sortea um valor diferente
        sort = 0
        while flag:
            flag = 0
            sort = randint(0, len(dados) - 1)
            for valor in valores:
                if(sort == valor):
                    flag = 1
                    break
        valores.append(sort)

        for j in range(0, QTD_COLUNAS):
            cluster_list[i]["centroide"].append(dados[sort][j+1])
    
    return cluster_list

def atualizarClusters(lista_antiga, nClusters):
    cluster_list = []
    media = []
    
    for coluna in range(0, QTD_COLUNAS):
        media.append(0)

    for i in range(0, nClusters):
        
        cluster_list.append({ 
            "centroide": [],
            "objs": []
        })
        for obj in lista_antiga[i]["objs"]:  
            for coluna in range(0, QTD_COLUNAS):
                media[coluna] += obj[coluna + 1]
        for coluna in range(0, QTD_COLUNAS):
            cluster_list[i]["centroide"].append(media[coluna]/len(lista_antiga[i]["objs"]))

        for coluna in range(0, QTD_COLUNAS):
            media[coluna] = 0
    
    return cluster_list

def euclides(centroide, obj):
    distancia = 0

    #para cada dado calcula a distancia euclidiana e soma
    for i in range(0, QTD_COLUNAS):
        distancia += pow( ( centroide["centroide"][i]) - obj[i+1], 2) # +1 por causa da lbl

    return sqrt(distancia)

def agruparObjetos(cluster_list, dados, nClusters):
    for obj in dados:
        menor_distancia = [0, 100000] #menor_distancia[0] = index do cluster, menor_distancia[1] = distancia
        
        #calcula distancia para cada cluster e escolhe a menor
        for i in range(0, nClusters):
            distancia = euclides(cluster_list[i], obj)
            if(distancia < menor_distancia[1]):
                menor_distancia[1] = distancia
                menor_distancia[0] = i
        cluster_list[ menor_distancia[0] ]["objs"].append(obj)

def imprimirClusters(cluster_list, nClusters):
    for i in range(0, nClusters):
        for obj in cluster_list[i]["objs"]:
            print(obj[0] + "\t" + str(i))

if __name__ == "__main__":
    nomeArquivo = input()
    nClusters = int(input())
    nInteracoes = int(input())

    #leitura dos dados do arquivo
    dados = lerArquivo(nomeArquivo)

    #inicia clusters sorteando 3 obj aleatórios
    cluster_list = inicializarClusters(dados)
    agruparObjetos(cluster_list, dados, nClusters)

    for i in range(0, nInteracoes):
        #agrupa os objetos aos clusters mais proximos

        cluster_list = atualizarClusters(cluster_list, nClusters)
        agruparObjetos(cluster_list, dados, nClusters)

    imprimirClusters(cluster_list, nClusters)
    
# 1.Escolher k centróides
# 2.Associar cada objeto x ao cluster com o centróide mais próximo
# 3.Recalcular os centróides
# 4.Repetir 2 se não chegou a 3 iterações
    
    
