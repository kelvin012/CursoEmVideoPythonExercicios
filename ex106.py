def ajuda(texto):
    modprint(f'Acessando o manual do comando {texto}')
    help(texto)


def modprint(text):
    print('~' * (len(text) + 4))
    print(f'  {text}  ')
    print('~' * (len(text) + 4))


while True:
    resposta = str(input('Função ou Biblioteca > '))

    if resposta == 'fim':
        modprint('ATÉ LOGO!')
        break
    else:
        ajuda(resposta)
