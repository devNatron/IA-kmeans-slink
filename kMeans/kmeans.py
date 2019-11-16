from random import randint

#variaveis globais
QTD_DADOS = 0

def abrirArquivo(nomeArquivo):
    arquivo = open("../datasets/" + nomeArquivo + ".txt", "r")
    return arquivo

def lerArquivo(nomeArquivo): 
    arquivo = abrirArquivo(nomeArquivo)
    dados = []
    
    labels = arquivo.readline().split()
    global QTD_DADOS
    QTD_DADOS = len(labels) - 1

    for linha in arquivo:
        obj = linha.split()
        for i in range(1, QTD_DADOS+1):
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

        for j in range(0, QTD_DADOS):
            cluster_list[i]["centroide"].append(dados[sort][j+1])
    
    return cluster_list

def euclides(centroide, obj):
    distancia = 0

    #para cada dado calcula a distancia euclidiana e soma
    for i in range(0, QTD_DADOS):
        distancia += pow( ( centroide["centroide"][i]) - obj[i+1], 2)

    return distancia

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


if __name__ == "__main__":
    nomeArquivo = input("Insira nome do arquivo: ")
    nClusters = int(input("Quantidade de clusters: "))
    #nInteracoes = input("quantidade de interacoes: ")

    #leitura dos dados do arquivo
    dados = lerArquivo(nomeArquivo)

    #inicia clusters sorteando 3 obj aleatórios
    cluster_list = inicializarClusters(dados)
    
    #agrupa os objetos aos clusters mais proximos
    agruparObjetos(cluster_list, dados, nClusters)

    print(cluster_list)
    # cluster_list[0]["objs"].append([dados[4][1], dados[4][2], dados[4][3]])
    
    #centroides = agrupar(centroides, dados)

# 1.Escolher k centróides
# 2.Associar cada objeto x ao cluster com o centróide mais próximo
# 3.Recalcular os centróides
# 4.Repetir 2 se não chegou a 3 iterações
    
    
