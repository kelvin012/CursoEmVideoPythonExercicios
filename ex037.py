numero = int(input('Digite um numero Inteiro! '))
print('Escolha a base para qual o numero {} sera convertido! '.format(numero))
print('[ 1 ] conversão para BINÁRIO')
print('[ 2 ] conversão para OCTAL')
print('[ 3 ] conversão para HEXADECIMAL')
base = int(input('Escolha uma opção: '))

if base == 1:
    print('O número {} convertido para base binária tem valor igual a {}'.format(numero, bin(numero)[2:]))
elif base == 2:
    print('O número {} convertido para base octal tem valor igual a {}'.format(numero, oct(numero)[2:]))
elif base == 3:
    print('O número {} convertido para base hexadecimal tem valor igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Opção invalida !')
