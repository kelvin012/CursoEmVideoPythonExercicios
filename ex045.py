from random import randint

print('#' * 40)
print('{}{}{}{}{}{}{}{}{}'.format('#', (' ' * 8), 'Pedra ', '|', ' Papel ', '|', ' Tesoura', (' ' * 7), '#'))
print('#' * 40)

pedra = 1
papel = 2
tesoura = 3
vitorioso = ''
computador = randint(1, 3)
jogador = int(input('1 -> Pedra\n2 -> Papel\n3 -> tesoura\nEscolha uma opção - > '))

if jogador == pedra and computador == papel:
    vitorioso = 'Computador Ganhou!'
elif jogador == papel and computador == tesoura:
    vitorioso = 'Computador Ganhou!'
elif jogador == tesoura and computador == pedra:
    vitorioso = 'Computador Ganhou!'
elif jogador == computador:
    vitorioso = 'Empate.'
else:
    vitorioso = 'Jogador Ganhou!'

if computador == 1:
    print('O computador jogou Pedra')
elif computador == 2:
    print('O computador jogou Papel')
else:
    print('O computador jogou Tesoura')

print('O resultado da partida foi o -> {}'.format(vitorioso))
