from random import randint

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
    valores = []
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
    nInteracoes = int(input("Quantidade de interacoes: "))

    #leitura dos dados do arquivo
    dados = lerArquivo(nomeArquivo)

    #inicia clusters sorteando 3 obj aleatórios
    cluster_list = inicializarClusters(dados)
    agruparObjetos(cluster_list, dados, nClusters)

    print("primeiros valores -------------------------------------")
    print(cluster_list)
    
    for i in range(0, nInteracoes):
        #agrupa os objetos aos clusters mais proximos
        print("iteracao " + str(i) + "-------------------------------------")
        print(cluster_list)

        cluster_list = atualizarClusters(cluster_list, nClusters)
        agruparObjetos(cluster_list, dados, nClusters)

    print("terminou -------------------------------------")
    print(cluster_list)
    
# 1.Escolher k centróides
# 2.Associar cada objeto x ao cluster com o centróide mais próximo
# 3.Recalcular os centróides
# 4.Repetir 2 se não chegou a 3 iterações
    
    
