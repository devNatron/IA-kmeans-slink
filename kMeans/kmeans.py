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
    #nClusters = input("quantidade de clusters: ")
    #nInteracoes = input("quantidade de interacoes: ")

    dados = lerArquivo(nomeArquivo)
    print(dados)
    #centroides = agrupar(centroides, dados)
    
    
