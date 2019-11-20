#variaveis globais
QTD_COLUNAS = 0

'''
	---------------------------------------
	Inicializacao e atualizacao de clusters
	---------------------------------------
''' 

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
    
def atualizaClusters():
	
	
	return cluster_list   
    
    
'''
	----------------------------------
	Funcoes de agrupamento e distancia
	----------------------------------
'''    
 
def singleLink(cluster1, cluster2):
	
	return distancia

def distEuclidiana(cluster1, cluster2):
	
	
	return dist


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
    kmin = int(input("Insira o kmin: "))
    kmax = int(input("Insira o kmax: "))

    #leitura dos dados do arquivo
    dados = lerArquivo(nomeArquivo)

    #inicia clusters com kmax particoes
    cluster_list = inicializarClusters(dados, kmax)
    
    print("primeiros valores -------------------------------------")
    print(cluster_list)
    
	#nao tenho certeza se vai ser len(cluster_list) mesmo
	#a gente precisa pegar a quantidade de clusters que tem atualmente
    quantClusters = len(cluster_list)
    
    while quantClusters > kmin:
		
		
		
		quantClusters = len(cluster_list)

	#gerar os kmin arquivos
    print("terminou -------------------------------------")
    print(cluster_list)
    
    
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
