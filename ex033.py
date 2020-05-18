a = float(input('Digite o numero 1 '))
b = float(input('Digite o numero 2 '))
c = float(input('Digite o numero 3 '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi -> {}'.format(menor))
print('O maior valor digitado foi -> {}'.format(maior))
