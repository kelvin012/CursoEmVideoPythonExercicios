def leiaint(msg):
    while True:
        n = input(msg)
        if str(n).isnumeric():
            break
        else:
            print('Error digite um número inteiro!')
    return n


print('--' * 15)
num = leiaint('Digite um número: ')
print(f'voccê acabou de digitar o número {num}')
