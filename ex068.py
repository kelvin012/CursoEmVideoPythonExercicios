from random import randint

print('=-' * 27)
print('{:º^54}'.format(' PAR OU ÍMPAR '))
print('=-' * 27)
wins = 0
while True:
    valor = int(input('Escolha um valor :> '))
    jogador = ' '
    while jogador not in 'PI':
        jogador = str(input('Par ou Ímpar?[ P/I ] ')).upper().strip()[0]
    pseudo_rng = int(randint(0, 10))
    soma = pseudo_rng + valor
    if soma % 2 == 0:
        poui = 'Par'
    else:
        poui = 'Ímpar'
    if (soma % 2 == 0 and jogador == 'P') or (soma % 2 != 0 and jogador == 'I'):
        print('--' * 27)
        print(f'Você jogou {valor} e o computador {pseudo_rng}. Total de {soma} deu {poui}!')
        print('--' * 27)
        print('Você GANHOU!')
        print('Vamos de novo....')
        print('=-' * 15)
        wins += 1
    else:
        print('--' * 27)
        print(f'Você jogou {valor} e o computador {pseudo_rng}. Total de {soma} deu {poui}!')
        print('--' * 27)
        print('Você PERDEU!')
        print('=-' * 27)
        break
print(f'O JOGO ACABOU! Você ganhou {wins} vez(es)')
