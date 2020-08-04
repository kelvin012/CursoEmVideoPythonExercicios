from datetime import date

pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
ano_nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - ano_nasc
num_ctps = int(input('Carteira de trabalho (0 não tem) '))
if num_ctps != 0:
    pessoa['ctps'] = num_ctps
    pessoa['contratação'] = int(input('Ano de contratção: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = (pessoa['contratação'] - ano_nasc) + 35
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
