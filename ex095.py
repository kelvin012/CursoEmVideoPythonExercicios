jogadores = list()

while True:
    jogador = dict()
    tot_gols = 0
    jogador['nome'] = str(input('Nome do jogador: '))
    qtd_partidas = int(input('Quantas partidas? '))
    gols = list()
    for i in range(0, qtd_partidas):
        num = int(input(f'Quantos gols na partida {i}? '))
        gols.append(num)
        tot_gols += num
    jogador['gols'] = gols[:]
    jogador['total'] = tot_gols
    jogadores.append(jogador.copy())
    pergunta = str(input('Deseja adicionar mais ? [S/N]')).lower().strip()[0]
    if pergunta != 's':
        break
print(jogadores)
print('-=' * 30)
print(f'cod {"nome":<10}{"gols":<18}{"total":<6}')
print('--' * 20)
for i in range(0, len(jogadores)):
    print(f'{i:>3} {jogadores[i]["nome"]:<10}{jogadores[i]["gols"]}{jogadores[i]["total"]:>7}')
while True:
    print('--' * 20)
    r = int(input('Mostrar dados de qual jogador? '))
    if r == 999:
        break
    elif 0 <= r <= len(jogadores):
        print(f'-- LEVAMENTO DO JOGADOR {jogadores[r]["nome"]}:')
        for j in range(0, len(jogadores[r]['gols'])):
            print(f'   No jogo {j} fez {jogadores[r]["gols"][j]} gols.')
    else:
        print(f'ERROR 404!Não existe jogador com código {r}! Tente novamente.')
print('--' * 20)
print('<< VOLTE SEMPRE >>')
