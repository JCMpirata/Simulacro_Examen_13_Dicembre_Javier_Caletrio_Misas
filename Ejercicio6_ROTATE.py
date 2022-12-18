matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def rotate(matriz, direccion):
    if direccion == "clockwise":

        matriz = matriz[::-1]
        for i in range(len(matriz)):
            for j in range(i):
                matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
        return matriz

    elif direccion == "counter-clockwise":
        matriz = matriz[::-1]
        for i in range(len(matriz)):
            for j in range(i):
                matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
        return matriz
