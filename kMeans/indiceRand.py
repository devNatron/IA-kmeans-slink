def abrirArquivo(nomeArquivo):
    arquivo = open("../datasets/" + nomeArquivo + ".txt", "r")
    return arquivo

def calcularIndice(cluster_list, nClusters):
    particao = []
    partRef = []
    cont = 0

    for i in range(0, nClusters):
        for obj in cluster_list[i]["objs"]:
            particao.append([obj[0], i])
    
    nomePart = input()
    arquivo = abrirArquivo(nomePart)

    for linha in arquivo:
        obj = linha.split()
        obj[1] = int(obj[1])
        partRef.append(obj)

    for obj in particao:
        for objRef in partRef:
            if(obj[0] == objRef[0]):
                obj.append(objRef[1])
                # print(obj)

    n = len(particao)
    for i in range(0, n):
        for j in range(i+1, n):
            if(particao[i][1] == particao[j][1] and particao[i][2] == particao[j][2]):
                cont = cont + 1
            elif(particao[i][1] != particao[j][1] and particao[i][2] != particao[j][2]):
                cont = cont + 1

    return ( cont / ((n * n-1)/2) )