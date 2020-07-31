numeros = list()
maior = menor = 0
for i in range(0, 5):
    numeros.append(int(input(f'Digite o valor da posição {i}: ')))
    if i == 0:
        maior = menor = numeros[i]
    else:
        if numeros[i] > maior:
            maior = numeros[i]
        if numeros[i] < menor:
            menor = numeros[i]
print('--' * 30)
print('Você digitou os números: ', end='')
print(*numeros, sep=', ')

print(f'O Maior valor digitado foi {maior} nas posições ', end='')
for pos, num in enumerate(numeros):
    if num == maior:
        print(f'{pos}... ', end='')
print()

print(f'O Menor valor digitado foi {menor} nas posiçoes ', end='')
for pos, num in enumerate(numeros):
    if num == menor:
        print(f'{pos}... ', end='')
print()
print('--' * 30)
