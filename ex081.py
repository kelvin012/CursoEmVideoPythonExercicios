numeros = list()
while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    pergunta = str(input('Você deseja adicionar mais números? ')).strip().lower()[0]
    if pergunta != 's':
        break
print('--' * (20 + len(numeros) * 2))
print(f'Foram digitados {len(numeros)} números')
print('O valores de forma ordenada são > ', end='')
print(*sorted(numeros, reverse=True), sep=', ')
if 5 in numeros:
    print(f'O valor 5 foi encontrado na lista!\nE ele esta no indice {numeros.index(5)} da lista')
else:
    print('O valor 5 não esta incluso na lista!')
print('--' * (20 + len(numeros) * 2))
