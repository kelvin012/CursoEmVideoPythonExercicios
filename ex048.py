soma = 0

for i in range(1, 500):
    if i % 2 != 0 and i % 3 == 0:
        soma += i

print('O Somatorio de todos os numeros Ímpares e que são Multiplos de 3 e igual a: {}'.format(soma))
