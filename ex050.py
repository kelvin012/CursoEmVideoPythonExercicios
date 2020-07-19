soma = 0
c = 0

for i in range(0, 6):
    n = int(input('Digite um numero Inteiro: '))
    if n % 2 == 0:
        soma += n
        c += 1

print('A soma de todos os {} numeros Pares digitados e equivalente a: {}'.format(c, soma))
