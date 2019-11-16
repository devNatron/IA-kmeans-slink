from random import randint

def abrirArquivo(nomeArquivo):
    arquivo = open("../datasets/" + nomeArquivo + ".txt", "r")
    return arquivo

def lerArquivo(nomeArquivo): 
    arquivo = abrirArquivo(nomeArquivo)
    dados = []
    
    for linha in arquivo:
        dados.append(linha.split())

    return dados

def agrupar(centroides, dados):
    for obj in dados:
        (centroides[0], obj)

if __name__ == "__main__":
    nomeArquivo = input("Insira nome do arquivo: ")
    nClusters = int(input("Quantidade de clusters: "))
    #nInteracoes = input("quantidade de interacoes: ")

    dados = lerArquivo(nomeArquivo)
    # print(dados)

    cluster_list = []
    for i in range(0, nClusters):       # inicializa uma lista de dicionarios 
        cluster_list.append({ 
            "centroide": [-1, -1, -1],
            "objs": []
        })

    for k in cluster_list:      # escolhe N objetos aleatorios para serem centroides iniciais 
        val = randint(1, len(dados))
        k["centroide"] = [dados[val][1], dados[val][2], dados[val][3]]

    # cluster_list[0]["objs"].append([dados[4][1], dados[4][2], dados[4][3]])
    
    #centroides = agrupar(centroides, dados)

# 1.Escolher k centróides
# 2.Associar cada objeto x ao cluster com o centróide mais próximo
# 3.Recalcular os centróides
# 4.Repetir 2 se não chegou a 3 iterações
    
    
