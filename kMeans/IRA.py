def abrirArquivo(nomeArquivo):
    arquivo = open("./" + nomeArquivo, "r")
    return arquivo


def indiceRand(arquivo, arquivoRef):
    particao = []
    partRef = []
    a = b = c = d = 0

    for linha in arquivo:
        obj = linha.split()
        obj[1] = int(obj[1])
        particao.append(obj)

    for linha in arquivoRef:
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
                a = a + 1
            elif(particao[i][1] != particao[j][1] and particao[i][2] != particao[j][2]):
                b = b + 1
            elif(particao[i][1] == particao[j][1] and particao[i][2] != particao[j][2]):
                c = c + 1
            else:
                d = d + 1

    m = a + b + c + d
    temp = (a + c)*(a + b)
    return ( (a - temp/m) / ((a + c + a + b)/2 - temp/m) )

if __name__ == "__main__":
    arquivo = input('Nome do arquivo da particao: ')
    arquivoRef = input('Nome do arquivo da particao referencia: ')

    particao = abrirArquivo(arquivo)
    partRef = abrirArquivo(arquivoRef)

    rand = indiceRand(particao, partRef)
    print(rand)