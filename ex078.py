numeros = list()

for i in range(0, 5):
    numeros.append(int(input(f'Digite o valor da posição {i}: ')))

print('Você digitou os números: ', end='')
print(*numeros, sep=', ')

maior = max(numeros)
print(f'O Maior valor digitado foi {maior} nas posições ', end='')
for pos, num in enumerate(numeros):
    if num == maior:
        print(f'{numeros.index(maior, pos, len(numeros))}... ', end='')
print()

menor = min(numeros)
print(f'O Menor valor digitado foi {menor} nas posiçoes ', end='')
for pos, num in enumerate(numeros):
    if num == menor:
        print(f'{numeros.index(menor, pos, len(numeros))}... ', end='')
print()
