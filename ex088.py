from random import randint
from time import sleep

print('--' * 20)
print('{: ^40}'.format('JOGA NA MEGA SENA'))
print('--' * 20)
jogos = []
qtd_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
for i in range(0, qtd_jogos):
    jogo = []
    c = 1
    while c <= 6:
        rng = randint(1, 60)
        if rng not in jogo:
            jogo.append(rng)
            c += 1
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
print('{}  SORTEANDO {} JOGOS  {}'.format('-=' * 4, len(jogos), '-=' * 4))
for i, jogo in enumerate(jogos):
    print(f'Jogo {i + 1}: {jogo}', end='')
    print()
    sleep(0.5)
print('{} < {} > {}'.format('-=' * 6, 'BOA SORTE!', '-=' * 5))
