def ficha(nome='<desconhecido>', gols='0'):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('--' * 15)
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))

if n != '' and g.isnumeric():
    ficha(n, g)
elif n != '' and g.isnumeric() == False:
    ficha(nome=n)
elif n == '' and g.isnumeric() == True:
    ficha(gols=g)
