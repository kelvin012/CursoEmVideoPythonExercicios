numeros = list()
for i in range(0, 5):
    num = int(input('Digite um número: '))
    if not numeros or num > numeros[i - 1]:
        numeros.append(num)
        print('Adicionado ao final da lista...')
    elif num < numeros[i - 1] and num < numeros[0]:
        numeros.insert(0, num)
        print('Adicionado na posição 0 da lista...')
    else:
        numeros.insert(1, num)
        print('Adicionado na posição 1 da lista...')
print('--' * 20)
print('Os Números ordenados foram > ', end='')
print(*numeros, sep=', ')
