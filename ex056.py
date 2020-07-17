sum_ages = 0
woman_less_than_twenty = 0
older_man_age = 0
older_man = ''
woman = 0

for i in range(0, 4):
    nome = str(input('Digite seu Nome > '))
    idade = int(input('Digite sua Idade > '))
    sexo = str(input('Qual o seu Sexo [ M ] / [ F ] > ')).lower()
    sum_ages += idade

    if sexo == 'm' and idade > older_man_age:
        older_man_age = idade
        older_man = nome

    if sexo == 'f' and idade < 20:
        woman_less_than_twenty += 1
    if sexo == 'f':
        woman += 1

media_idade = sum_ages / 4
print('A Media de idade dessas 4 pessoas vale > {}'.format(media_idade))

if older_man != '':
    print('Dentre essas pessoas o Homem mais velho é o Sr. {} o qual possui {} Anos'.format(older_man, older_man_age))

if woman != 0:
    print('Dentre essas pessoas existem {} pessoas do sexo feminino que possuem menos de 20 Anos!'.format(
        woman_less_than_twenty))
