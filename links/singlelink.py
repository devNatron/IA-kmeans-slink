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

    for i in range(len(dados)):
        cluster_list.append([])
        for j in range(len(dados)):
            cluster_list[i].append(distEuclidiana(dados[i], dados[j]))

    return cluster_list


def atualizaClusters(cluster_list):
    menor = cluster_list[0][1]
    cluster = []
    pos = ({
        "x": 0,
        "y": 1
    })
    for i in range(len(cluster_list)):
        for j in range(len(cluster_list[i])):
            if(cluster_list[i][j] != 0 and cluster_list[i][j] < menor):
                menor = cluster_list[i][j]
                pos["x"] = i
                pos["y"] = j
                
    for i in range(len(cluster_list[pos["x"]])):
        if(cluster_list[pos["x"]][i] != 0 and cluster_list[pos["y"]][i] != 0):
            menorDist = min(cluster_list[pos["x"]][i], cluster_list[pos["y"]][i])
            cluster.append(menorDist)
    cluster.insert(0, 0.0)
    del cluster_list[pos["x"]]
    del cluster_list[pos["y"]-1]

    for i in range(len(cluster_list)):
        del cluster_list[i][pos["x"]]
        del cluster_list[i][pos["y"]-1]

    cluster_list.insert(0, cluster)
    for i in range(1, len(cluster_list)):
        cluster_list[i].insert(0, cluster[i])
    return cluster_list


'''
	----------------------------------
	Funcoes de agrupamento e distancia
	----------------------------------
'''
def distEuclidiana(cluster1, cluster2):
    distancia = 0

    # para cada dado calcula a distancia euclidiana e soma
    for i in range(1, QTD_COLUNAS+1):
        distancia += pow((cluster1[i] - cluster2[i]), 2)

    return sqrt(distancia)


'''
	----------------------------------
	Funcoes para trabalhar com arquivo
	(Usando as que os cara criaram)
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


if __name__ == "__main__":
    nomeArquivo = input("Insira nome do arquivo: ")
    #kmin = int(input("Insira o kmin: "))
    #kmax = int(input("Insira o kmax: "))

    # leitura dos dados do arquivo
    dados = lerArquivo(nomeArquivo)

    # inicia clusters com kmax particoes
    cluster_list = inicializarClusters(dados)

    print("primeiros valores -------------------------------------")
    print(len(cluster_list), ' Clusters: ', cluster_list, '\n\n')

    # nao tenho certeza se vai ser len(cluster_list) mesmo
    # a gente precisa pegar a quantidade de clusters que tem atualmente
    quantClusters = 10000
    while quantClusters > 1:
        atualizaClusters(cluster_list)
        quantClusters = len(cluster_list)
        print(len(cluster_list), ' Clusters: ', cluster_list, '\n\n')
        
    # gerar os kmin arquivos


'''   
	Talvez dê para reaproveitar?

    for i in range(0, nInteracoes):
        #agrupa os objetos aos clusters mais proximos
        print("iteracao " + str(i) + "-------------------------------------")
        print(cluster_list)

        cluster_list = atualizarClusters(cluster_list, nClusters)
        agruparObjetos(cluster_list, dados, nClusters)
'''

'''
	Algoritmo:
	* Inicia com cada objeto em um cluster
	* Enquanto há cluster para agrupar
		- Calcula distância entre cada par de clusters
		- Combina o par de clusters mais próximo
'''
