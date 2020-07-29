extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    print('--' * 15)
    n = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= n <= 20:
        print(f'Você digitou o número {str(extenso[n]).capitalize()}')
    else:
        print('Tente Novamente. ', end='')
    print('--' * 15)
    pergunta = str(input('Você quer verificar outro número ? ')).upper().strip()[0]
    if pergunta != 'S':
        break
