matriz = []
for i in range(0, 3):
    linha = []
    for j in range(0, 3):
        linha.append(int(input(f'Digite um valor paara [{i}, {j}]: ')))
    matriz.append(linha[:])
    linha.clear()
print('-=' * 17)
for linha in matriz:
    for elemento in linha:
        print('[ {} ]'.format(elemento), end='')
    print()
