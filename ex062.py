a1 = int(input('Digite o primeiro termo da progessão: '))
r = int(input('Digite a Razão da progressão: '))
decimo = a1 + (10 - 1) * r
c = 0
pergunta = ''
ultimo = 0

while pergunta != 'n':

    while c < 10:
        An = a1 + (c - 1) * r
        print('{}'.format(An + r), end=' -> ')
        c += 1
    print('FIM')
    pergunta = str(input('\nVoce deseja mostra mais termos ? '))
    if pergunta == 's':
        termos = int(input('Digite quantos termos a mais você deseja mostrar : '))
        ultimo += termos
        while c < ultimo + termos:
            An = a1 + (c - 1) * r
            print('{}'.format(An + r), end=' -> ')
            c += 1
    else:
        pergunta = 'n'
# print('FIM')
