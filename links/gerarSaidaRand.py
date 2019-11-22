import numpy as np
def abrirArquivo():
    arquivo = open("./rand/monkeySaidaSingleLink_8C.clu", "r")
    return arquivo


def lerArquivo():
    arquivo = abrirArquivo()
    labels = []
    dados = []
    labels = arquivo.readlines()

    arquivo = open("./rand/teste_8C.clu", "w")
    for i in range(len(labels)):
        dados.append([])
        dados[i].append(sorted(labels[i].split()))
        vetor = np.asarray(dados[i])
        for j in range(len(vetor)):
            for k in range(len(vetor[j])):
                arquivo.write(str(vetor[j][k]) + "\t" + str(i+1) + "\n")
    arquivo.close()
        
    
    

if __name__ == "__main__":
    # leitura dos dados do arquivo
    lerArquivo()
