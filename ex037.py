numero = int(input('Digite um numero Inteiro! '))
base = int(input('Escolha a base para qual o numero {} sera convertido! '.format(numero)))

if base == 1:
    print('O número {} convertido para base binária tem valor igual a {}'.format(numero, bin(numero)))
elif base == 2:
    print('O número {} convertido para base octal tem valor igual a {}'.format(numero, oct(numero)))
elif base == 3:
    print('O número {} convertido para base hexadecimal tem valor igual a {}'.format(numero
                                                                                     , hex(numero)))
else:
    print('Opção invalida !')
