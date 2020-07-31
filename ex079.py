numeros = list()
print('--' * 20)
while True:
    num = int(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
    else:
        print(f'O número {num} ja esta na lista!\nNão e permitido duplicata!')
        print('--' * 20)
    pergunta = str(input('Deseja adicionar mais números? ')).strip().upper()[0]
    print('--' * 20)
    if pergunta != 'S':
        break
print('Você adicionou os números > ', end='')
print(*sorted(numeros), sep=',')
print('--' * 20)
