matriz = []
soma_par = soma_coluna3 = maior_linha2 = 0
for i in range(0, 3):
    linha = []
    for j in range(0, 3):
        num = int(input(f'Digite um valor para [{i}, {j}]: '))
        linha.append(num)
        if num % 2 == 0:
            soma_par += num
        if j == 2:
            soma_coluna3 += num
    if i == 1:
        for indice in range(0, 3):
            if indice == 0:
                maior_linha2 = linha[indice]
            else:
                if linha[indice] > maior_linha2:
                    maior_linha2 = linha[indice]
    matriz.append(linha[:])
    linha.clear()
print('-=' * 17)
for linha in matriz:
    for elemento in linha:
        print('[ {:^5} ]'.format(elemento), end='')
    print()
print('-=' * 17)
print(f'A soma dos valores pares é {soma_par}.')
print(f'A soma dos valores da terceira coluna é {soma_coluna3}.')
print(f'O maior valor da segunda linha é {maior_linha2}.')
print('-=' * 17)
