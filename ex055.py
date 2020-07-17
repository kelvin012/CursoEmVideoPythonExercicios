maiorPeso = 0
menorPeso = 0
tester = 0

for i in range(0, 5):
    peso = float(input('Digite o Peso: '))

    if peso > maiorPeso:
        maiorPeso = peso

    if tester != 1:
        if menorPeso < peso:
            menorPeso = peso
        tester = 1
    else:
        if peso < menorPeso:
            menorPeso = peso

print('Maior Peso entre os digitados foi de : {}KG'.format(maiorPeso))
print('Menor Peso entre os digitados foi de : {}KG'.format(menorPeso))
