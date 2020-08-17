from time import sleep


def ajuda(texto):
    modprint(f'Acessando o manual do comando \'{texto}\'')
    help(texto)
    sleep(2)


def modprint(text):
    print('~' * (len(text) + 4))
    print(f'  {text}  ')
    print('~' * (len(text) + 4))
    sleep(1)


while True:
    resposta = str(input('Função ou Biblioteca > '))

    if resposta.upper() == 'FIM':
        modprint('ATÉ LOGO!')
        break
    else:
        ajuda(resposta)
