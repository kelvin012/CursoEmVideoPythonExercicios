n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))
n3 = int(input('Digite um número: '))
n4 = int(input('Digite um número: '))
nums = (n1, n2, n3, n4)
print('Você digitou os números: ', end='')
for pos, n in enumerate(nums):
    if pos != 3:
        print(n, end=', ')
    else:
        print(n)
print(f'O valor 9 apareceu {nums.count(9)} vezes')
if nums.count(3) != 0:
    print(f'O valor 3 apareceu pela primeira vez na {nums.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado nenhuma vez!')
print('Os números PARES digitados foram: ', end='')
for pos, n in enumerate(nums):
    if n % 2 == 0:
        print(n, end=' ')
