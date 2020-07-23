sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Qual o seu sexo ? ')).upper().strip()[0]
    if sexo != 'M' and sexo != 'F':
        print('Você digitou {} o que não e uma opção valida! por favor tente novamente > [M / F]!'.format(sexo))
print('Seu sexo é > {}'.format(sexo))
