pessoas = list()
dados = list()
maior = menor = total = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    total += 1
    pergunta = str(input('Quer continuar? ')).strip().lower()[0]
    if pergunta != 's':
        break
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
