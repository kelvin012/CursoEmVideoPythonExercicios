from datetime import date

nascimento = int(input('Digite o ano em que você Nasceu : '))
anoAtual = date.today().year

if anoAtual - nascimento < 18:
    i = nascimento + 18 - anoAtual
    print('Calma Soldado ainda faltam {} anos para que você se aliste no exercito Brasileiro SELVA!'.format(i))
elif anoAtual - nascimento == 18:
    print('Prepare-se SOLDADO voce ira para guerra o exercito Brasileiro aguarda anciosamente sua inscrição')
else:
    j = (nascimento + 18 - anoAtual) * -1
    print('SOLDADO ja passou {} anos da data de você se apresentar!'.format(j))
