print('{:¬^40}'.format(' LOJAS MONODEDOS '))

preço = float(input('Digite o preço total das compras: '))
print('#' * 50)
print('Escolha uma forma de pagamento!')
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
    parcela = preço / 2
    print('Sua compra sera parcelada em {}x de R${:.2f} SEM JUROS'.format(2, parcela))
    print('O valor total a ser pago no final será de R${:.2f}'.format(preço))
elif condição == 4:
    total = preço + ((preço * 20) / 100)
    totalParcelas = int(input('Quantas parcelas? '))
    parcela = total / totalParcelas
    print('Sua compra sera parcelada em {}x de R${:.2f} COM JUROS'.format(totalParcelas, parcela))
    print('O valor final pago neste parcelamento será de R${:.2f}'.format(total))
else:
    print('Opção {} invalida tente novamente!'.format(condição))
