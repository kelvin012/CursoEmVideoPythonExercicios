'''numero = 7
fatorial = 0
opr = 0
test = 0

while numero > 0:
    # opr = numero * (numero - 1)
    if test == 0:
        fatorial = numero * (numero - 1)
        test = 1
    else:
        fatorial = fatorial * (numero - 1)
    print(fatorial)
    #opr += fatorial

    #print(opr)
    numero -= 1
print('OPR : {}'.format(opr))
print('\nO Fatorial de {} é igual a > {}'.format(numero, fatorial))
'''

#nao fiz