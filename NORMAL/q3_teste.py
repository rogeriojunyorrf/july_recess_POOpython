#transposta

matriz = []
tmatriz = []
n = 2
for i in range(n):
    linha = []
    for j in range(n):
        linha.append(int(input('Entre com um valor inteiro: ')))
    matriz.append(linha)

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(0)
    tmatriz.append(linha)

for i in range(n):
    for j in range(n):
        tmatriz[i][j] = matriz[j][i]
    
for i in range(n):
    print(matriz[i])

print()

for i in range(n):
    print(tmatriz[i])




