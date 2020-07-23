r = 'S'
somatorio = 0
qtd_numeros = 0
maior = 0
menor = 0
control = 0
while r == 'S':
    num = int(input('Digite um número: '))
    qtd_numeros += 1
    somatorio += num
    if num > maior:
        maior = num

    if control != 1:
        if menor < num:
            menor = num
        control = 1
    else:
        if num < menor:
            menor = num
    r = str(input('Você deseja continuar ? [S/N] > ')).upper().strip()[0]
media = somatorio / qtd_numeros
print('A media entre os {} valore(s) digitados é igual a > {:.2f}'.format(qtd_numeros, media))
print('O Maior valor digitado foi {} e o Menor foi {}'.format(maior, menor))
