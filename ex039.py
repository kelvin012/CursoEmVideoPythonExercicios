from datetime import date

sexo = str(input('Qual o seu sexo ?\n Digite [ F ] para Feminino e [ M] para Masculino\n>')).upper()

if sexo == 'M':

    nascimento = int(input('Digite o ano em que você Nasceu : '))
    anoAtual = date.today().year

    if anoAtual - nascimento < 18:
        i = nascimento + 18 - anoAtual
        print('Calma Soldado ainda faltam {} ano(s) para que você se aliste no exercito Brasileiro. SELVA!'.format(i))
        print('Seu alistamento sera no ano de {}'.format(nascimento + 18))
    elif anoAtual - nascimento == 18:
        print('Prepare-se SOLDADO você vai para guerra, o exercito Brasileiro aguarda anciosamente sua inscrição!')
    else:
        j = (nascimento + 18 - anoAtual) * -1
        print('SOLDADO ja passou {} ano(s) da data de você se apresentar!'.format(j))
        print(
            'Você deveria ter se alistado no ano de {} , Aguardamos ansiosamente sua inscrição'.format(nascimento + 18))
elif sexo == 'F':
    print(
        'Mulheres fazem parte da nata da sociedade portanto de acordo com a nossa magnifica constituição de 88 nao ha necessidade do alistamento obrigatorio!')
else:
    print('Você não digitou um sexo valido Tente novamente!')
