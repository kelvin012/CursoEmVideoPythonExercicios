produto = float(input('Qual o valor do produto ? R$'))
aPrazo = produto + ((produto * 8) / 100)
aVista = produto - ((produto * 13) / 100)
print('O valor final do produto caso pague a vista sera de R${:.2f} caso parcele o valor total sera de R${:.2f}'.format(aVista, aPrazo))
