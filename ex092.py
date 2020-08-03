from datetime import date

pessoa = dict()
nome = str(input('Nome: '))
pessoa['nome'] = nome
ano_nasc = int(input('Ano de Nascimento: '))
pessoa['idade'] = date.today().year - ano_nasc
num_ctps = int(input('Carteira de trabalho (0 não tem) '))
if num_ctps != 0:
    pessoa['ctps'] = num_ctps
    ano_contratado = int(input('Ano de contratção: '))
    salario = float(input('Salário: R$ '))
    pessoa['contratação'] = ano_contratado
    pessoa['salário'] = salario
    pessoa['aposentadoria'] = (ano_contratado - ano_nasc) + 35
print(pessoa)
for k, v in pessoa.items():
    print(f'{k} tem o valor {v}')
