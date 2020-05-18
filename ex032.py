from datetime import date

ano = int(input('Digite o Ano o qual você quer analisar!coloque 0 caso queira analisar o ano atual -> '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(
        'O Ano de {} e um ano BISEXTO! \nPortanto tera 366 dias ao inves dos normais 355 a qual estamos acostumados!'.format(
            ano))
else:
    print('O Ano de {} e só mais um ano normal!'.format(ano))
