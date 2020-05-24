preço = float(input('Digite o preço do produto: '))
print('#' * 50)
print('1 -> Á vista dinheiro/cheque : 10% de desconto')
print('2 -> Á vista no cartão : 5% de desconto')
print('3 -> Em ate 2X no cartão sem juros')
print('4 -> 3X ou mais no cartão 20% de juros')
print('#' * 50)
condição = int(input('Digite a forma de pagamento: '))

if condição == 1:
    preço = preço - ((preço * 10) / 100)
    print('O valor a ser pago a vista corresponde a R${:.2f}'.format(preço))
elif condição == 2:
    preço = preço - ((preço * 5) / 100)
    print('O valor a ser pago a vista no cartão corresponde a R${:.2f}'.format(preço))
elif condição == 3:
    print('O valor a ser pago parcelado em 2X será de R${:.2f}'.format(preço))
elif condição == 4:
    preço = preço + ((preço * 20) / 100)
    print('O valor total do parcelamento em 3X ou mais vezes será de R${:.2f}'.format(preço))
else:
    print('Opção {} invalida tente novamente!'.format(condição))
