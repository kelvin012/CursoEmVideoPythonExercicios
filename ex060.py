n = int(input('Digite um número para mostrar seu Fatorial > '))
c = n
f = 1
print('Calculando o Fatorial de {}! => '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('{}'.format(f))
