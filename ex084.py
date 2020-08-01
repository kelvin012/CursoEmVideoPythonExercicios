pessoas = list()
dados = list()
maior = menor = total = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    total += 1
    pergunta = str(input('Quer continuar? ')).strip().lower()[0]
    if pergunta != 's':
        break
for i in range(0, len(pessoas)):
    if i == 0:
        maior = menor = pessoas[i][1]
    else:
        if pessoas[i][1] > maior:
            maior = pessoas[i][1]
        if pessoas[i][1] < menor:
            menor = pessoas[i][1]
print('--' * 20)
print(f'Você cadastrou {total} Pessoas no total.')
print(f'O Maior peso foi de {maior:.1f}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'[{pessoa[0]}]', end=' ')
print()
print(f'O Menor peso foi de {menor:.1f}Kg. Peso de ', end='')
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'[{pessoa[0]}]', end=' ')
print()
print('--' * 20)
