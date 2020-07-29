brasileirao = (
    'Coritiba', 'Flamengo', 'Sport Recife', 'Fluminense', 'Corinthians', 'Internacional',
    'Atlético-MG', 'Botafogo', 'Ceará SC', 'Goiás', 'São Paulo', 'Fortaleza', 'Bahia',
    'Grêmio', 'Athletico-PR', 'Bragantino-SP', 'Santos', 'Atlético-GO', 'Palmeiras', 'Vasco da Gama',)

print('-=' * 30)
print(f'Lista de times do Brasileirão Série A > ', end='')
for pos, time in enumerate(brasileirao):
    if pos != 19:
        print(f'{time}', end=', ')
    else:
        print(f'{time}.')

print('-=' * 30)
cinco_primeiros = brasileirao[0:5]
print(f'Os 5 primeiros colocados da tabela são > ', end='')
for pos, time in enumerate(cinco_primeiros):
    if pos != 4:
        print(f'{time}', end=', ')
    else:
        print(f'{time}.')

print('-=' * 30)
quatro_ultimos = brasileirao[-4:]
print(f'Os 4 ultimos colocados são > ', end='')
for pos, time in enumerate(quatro_ultimos):
    if pos != 3:
        print(f'{time}', end=', ')
    else:
        print(f'{time}.')

print('-=' * 30)
times_ordenados = sorted(brasileirao)
print(f'Os times do Brasileirão série A ordenados Alfabeticamente são > ', end='')
for pos, time in enumerate(times_ordenados):
    if pos != 19:
        print(f'{time}', end=', ')
    else:
        print(f'{time}.')

print('-=' * 30)
posicao_time = brasileirao.index('Flamengo') + 1
print(f'O Flamengo esta na {posicao_time}ª posição da tabela')
