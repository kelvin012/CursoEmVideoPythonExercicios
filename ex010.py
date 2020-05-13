money = float(input('Digite quantos merréis você tem? R$'))
dollar = money / 3.27
euro = money / 6.39
print(
    'A quantidade de R${:.2f} merréis consegue comprar U${:.2f} dollars americanos na cotação vigente de maio de 2017'.format(money, dollar))
print('A quantidade de R${:.2f} merréis consegue comprar {:.2f} Euros na cotação vigente 12 de maio de 2020'.format(money, euro))
