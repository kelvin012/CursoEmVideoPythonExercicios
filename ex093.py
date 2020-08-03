jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
qtd_partidas = int(input('Quantas partidas? '))
gols = list()
tot_gols = 0
for i in range(0, qtd_partidas):
    num = int(input(f'Quantos gols na partida {i}? '))
    gols.append(num)
    tot_gols += num
jogador['gols'] = gols[:]
jogador['total'] = tot_gols
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for pos, valor in enumerate(jogador['gols']):
    print(f'    => N partida {pos}, fez {valor} gols.')
print(f'foi um total de {jogador["total"]} gols.')
