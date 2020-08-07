from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores dda lista: ', end='')
    for i in range(0, 5):
        pseudo_rng = randint(1, 100)
        print(f'{pseudo_rng} ', end='')
        lista.append(pseudo_rng)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    print(f'Somando os valores pares de {lista}, temos ', end='')
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'{soma}')


numeros = []
sorteia(numeros)
somaPar(numeros)
