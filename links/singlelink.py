from math import sqrt

# variaveis globais
QTD_COLUNAS = 0

'''
	---------------------------------------
	Inicializacao e atualizacao de clusters
	---------------------------------------
'''


def inicializarClusters(dados):
    cluster_list = []
    #Inicializa uma lista de objetos, sendo cada um deles um cluster com seus respectivos dados
    for i in range(len(dados)):
        cluster_list.append({
            "Cluster": [],
            "Distancias": []
        })
        #Salva os nomes de cada objeto em um cluster pra cada
        cluster_list[i]["Cluster"].append(dados[i][0])

        #Calcula as distancias euclidianas de cada objeto e salva no vetor de distancias
        for j in range(len(dados)):
            cluster_list[i]["Distancias"].append(distEuclidiana(dados[i], dados[j]))

    return cluster_list


def atualizaClusters(cluster_list):
    menor = cluster_list[0]["Distancias"][1]
    #Inicialização do novo cluster 
    cluster = {
        "Cluster": [],
        "Distancias": []
    }
    #Variavel para salvar a posição dos dois clusters que serão agrupados
    pos = ({
        "x": 0,
        "y": 1
    })
    #Calcula a menor distancia que não seja 0 para o agrupamento
    for i in range(len(cluster_list)):
        for j in range(len(cluster_list[i]["Distancias"])):
            if(cluster_list[i]["Distancias"][j] != 0 and cluster_list[i]["Distancias"][j] < menor):
                menor = cluster_list[i]["Distancias"][j]
                pos["x"] = i
                pos["y"] = j

    #Salva as novas distâncias no novo cluster
    for i in range(len(cluster_list[pos["x"]]["Distancias"])):
        if(cluster_list[pos["x"]]["Distancias"][i] != 0 and cluster_list[pos["y"]]["Distancias"][i] != 0):
            menorDist = min(cluster_list[pos["x"]]["Distancias"][i], cluster_list[pos["y"]]["Distancias"][i])
            cluster["Distancias"].append(menorDist)
    cluster["Distancias"].insert(0, 0.0)

    #Salva os nomes presentes no novo cluster
    for i in range(len(cluster_list[pos["x"]]["Cluster"])):
        cluster["Cluster"].append(cluster_list[pos["x"]]["Cluster"][i])
    for i in range(len(cluster_list[pos["y"]]["Cluster"])):
        cluster["Cluster"].append(cluster_list[pos["y"]]["Cluster"][i])

    #Deleta clusters que foram agrupados
    if(pos["x"] < pos["y"]):
        del cluster_list[pos["y"]]
        del cluster_list[pos["x"]]
    else:
        del cluster_list[pos["x"]]
        del cluster_list[pos["y"]]

    #Deleta distancias dos clusters que agruparam de cada cluster
    for i in range(len(cluster_list)):
        if(pos["x"] < pos["y"]):
            del cluster_list[i]["Distancias"][pos["y"]]
            del cluster_list[i]["Distancias"][pos["x"]]
        else:
            del cluster_list[i]["Distancias"][pos["x"]]
            del cluster_list[i]["Distancias"][pos["y"]]
            
    #Insere o novo cluster na lista
    cluster_list.insert(0, cluster)
    for i in range(1, len(cluster_list)):
        cluster_list[i]["Distancias"].insert(0, cluster["Distancias"][i])
    return cluster_list


'''
	----------------------------------
	Funcoes de agrupamento e distancia
	----------------------------------
'''


def distEuclidiana(cluster1, cluster2):
    distancia = 0
    #Calcula para cada dado a distancia euclidiana e soma
    for i in range(1, QTD_COLUNAS+1):
        distancia += pow((cluster1[i] - cluster2[i]), 2)

    return sqrt(distancia)


'''
	----------------------------------
	Funcoes para trabalhar com arquivo
	----------------------------------
'''


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

def imprimirClusters(cluster_list, nClusters, nomeArquivo):
    arquivo = open("./rand/" + nomeArquivo + "SaidaSingleLinkParaRand_" + str(nClusters) + "C.clu", "w")
    for i in range(0, len(cluster_list)):
        cluster_list[i]["Cluster"] = sorted(cluster_list[i]["Cluster"])
        for j in range(0, len(cluster_list[i]["Cluster"])):
            arquivo.write(str(cluster_list[i]["Cluster"][j]) + "\t" + str(i) + "\n")
    arquivo.close()
    
if __name__ == "__main__":
    nomeArquivo = input("Insira nome do arquivo: ")
    kmin = int(input("Insira o kmin: "))
    kmax = int(input("Insira o kmax: "))

    # leitura dos dados do arquivo
    dados = lerArquivo(nomeArquivo)

    cluster_list = inicializarClusters(dados)
    quantClusters = kmax
    while quantClusters > kmin:
        atualizaClusters(cluster_list)
        quantClusters = len(cluster_list)
        if(len(cluster_list) <= kmax):
            imprimirClusters(cluster_list, quantClusters, nomeArquivo)


