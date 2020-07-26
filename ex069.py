over_18_years = 0
man = 0
woman_under_20 = 0
while True:
    print('--' * 15)
    print('{:º^30}'.format(' CADASTRE UMA PESSOA '))
    print('--' * 15)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).lower()
    if idade > 18:
        over_18_years += 1
    if sexo == 'm':
        man += 1
    if sexo == 'f' and idade < 20:
        woman_under_20 += 1
    while True:
        print('--' * 15)
        pergunta = str(input('Quer continuar? '))
        if pergunta == 's' or pergunta == 'n':
            break
    if pergunta == 'n':
        print('--' * 15)
        break
print('{:-^30}'.format(' FIM DO PROGAMA '))
print(f'Existem {over_18_years} pessoa(s) com mais de 18 anos nessa amostragem!')
print(f'Foram registrados {man} homem(s)')
print(f'Temos {woman_under_20} mulher(es) com  menos de 20 anos')
