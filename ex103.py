def ficha(nome='<desconhecido>', gols='0'):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('--' * 15)
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
ficha(n, g)
