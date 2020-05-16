ano = int(input('Digite o Ano em que você se encontra! '))
if ano % 4 == 0:
    print(
        'O Ano de {} e um ano bisexto portanto tera 366 dias ao inves dos normais 355 a qual estamos acostumados!'.format(ano))
else:
    print('O Ano de {} e só mais um ano normal!'.format(ano))
