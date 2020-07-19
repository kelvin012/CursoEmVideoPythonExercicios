from datetime import date

anoAtual = date.today().year
menor = 0
maior = 0

for i in range(0, 7):
    anoNasc = int(input('Digite o ano de Nascimento: '))
    idade = anoAtual - anoNasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1

print('{} pessoa(s) ja atigiram a maioridade de 21 anos é {} ainda irão atingir!'.format(maior, menor))
