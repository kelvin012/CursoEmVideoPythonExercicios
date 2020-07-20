num = 0
soma = 0
numeros = 0
while num != 999:
    num = int(input('Digite um número: '))
    if num != 999:
        soma += num
        numeros += 1
print('Você digitou {} números e a soma de todos eles vale : {}'.format(numeros, soma))
