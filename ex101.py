from datetime import date


def voto(age):
    voto = ''
    if 18 <= age <= 70:
        voto = 'OBRIGATÓRIO'
    elif age < 16:
        voto = 'NEGADO'
    else:
        voto = 'VOTO OPCIONAL'
    return voto


print('--' * 15)
nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - nasc
print(f'Com {idade} anos: {voto(idade)}')
