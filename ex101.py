from datetime import date


def voto(age):
    if 18 <= age < 70:
        v = 'VOTO OBRIGATÓRIO'
    elif age < 16:
        v = 'VOTO NEGADO'
    else:
        v = 'VOTO OPCIONAL'
    return v


print('--' * 15)
nasc = int(input('Em que ano você nasceu? '))
idade = date.today().year - nasc
print(f'Com {idade} anos: {voto(idade)}')
