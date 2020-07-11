from random import randint
from time import sleep

print('#' * 40)
print('{}{}{}{}{}{}{}{}{}'.format('#', (' ' * 8), 'Pedra ', '|', ' Papel ', '|', ' Tesoura', (' ' * 7), '#'))
print('#' * 40)
opçoes = ['Pedra', 'Papel', 'Tesoura']
computador = randint(0, 2)
jogador = int(input('0 -> Pedra\n1 -> Papel\n2 -> tesoura\nEscolha uma opção - > '))
print('PEDRA')
sleep(1)
print('PAPEL')
sleep(1)
print('TESOURA')
sleep(1)
if jogador == 0 or jogador == 1 or jogador == 2:
    if opçoes[jogador] == opçoes[0] and opçoes[computador] == opçoes[1]:
        resultado = 'Computador Ganhou!'
    elif opçoes[jogador] == opçoes[1] and opçoes[computador] == opçoes[2]:
        resultado = 'Computador Ganhou!'
    elif opçoes[jogador] == opçoes[2] and opçoes[computador] == opçoes[0]:
        resultado = 'Computador Ganhou!'
    elif opçoes[jogador] == opçoes[computador]:
        resultado = 'Empate.'
    else:
        resultado = 'Jogador Ganhou!'
    print('=+' * 12)
    print('O Computador jogou {}\nJogador escolheu {}'.format(opçoes[computador], opçoes[jogador]))
    print('=+' * 12)
    print('O resultado da partida foi o -> {}\n'.format(resultado))
else:
    print('Opção invalida!')
