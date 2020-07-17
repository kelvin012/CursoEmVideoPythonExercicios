numero = int(input('Digite um numero Inteiro: '))

if numero % 1 == numero and numero % numero == 1:
    print('O Número {} é um Número primo'.format(numero))
else:
    print('O Número {} não é um Número primo'.format(numero))
