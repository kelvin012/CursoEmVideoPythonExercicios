numero = int(input('Digite um numero Inteiro: '))
primo = 0
for i in range(1, numero + 1):
    if numero % i == 0:
        primo += 1
print('O Número {} foi divisivel {} vezes'.format(numero, primo))
if primo == 2:
    print('Portanto ele É um número PRIMO')
else:
    print('Portanto ele NÃO é PRIMO')
