numeros = [[], []]
for i in range(0, 7):
    num = int(input(f'Digite o {i + 1}º valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
print('A Sub Lista com os números PARES e igual a > ', end='')
print(*sorted(numeros[0]), sep=', ')
print('A Sub Lista com os números ÍMPARES e igual a > ', end='')
print(*sorted(numeros[1]), sep=', ')
