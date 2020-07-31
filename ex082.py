numeros = list()
pares = list()
impares = list()
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    pergunta = str(input('Você deseja continuar? ')).strip().lower()[0]
    if pergunta != 's':
        break
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print('Você digitou os números > ', end='')
print(*sorted(numeros), sep=', ')
print('Os números PARES digitados foram ', end='')
print(*sorted(pares), sep=', ')
print('Os números IMPARES digitados foram ', end='')
print(*sorted(impares), sep=', ')
