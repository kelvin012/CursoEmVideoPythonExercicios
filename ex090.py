aluno = dict()
nome = str(input('Nome: '))
media = float(input(f'Média de {nome}: '))
aluno['nome'] = nome
aluno['media'] = media
if media >= 6:
    aluno['situa'] = 'Aprovado'
else:
    aluno['situa'] = 'Reprovado'
print(f'Nome é igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')
print(f'Situação é igual a {aluno["situa"]}')
