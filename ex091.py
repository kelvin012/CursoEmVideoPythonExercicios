from random import randint
from time import sleep

jogadores = dict()
for i in range(1, 5):
    jogadores['jogador' + str(i)] = randint(1, 6)
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(0.6)
print('Ranking dos jogadores:')
count = 1
for item in sorted(jogadores, key=jogadores.get, reverse=True):
    print(f'{count}º lugar {item} com {jogadores[item]}')
    sleep(0.3)
    count += 1
