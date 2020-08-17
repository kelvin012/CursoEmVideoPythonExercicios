def leiaint(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            break
        else:
            print('Error digite um número inteiro!')
    return n


print('--' * 15)
num = int(leiaint('Digite um número: '))
print(f'voccê acabou de digitar o número {num}')
