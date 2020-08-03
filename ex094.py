pessoas = list()
soma_idade = 0
woman = list()
while True:
    dados = dict()
    nome = str(input(('Nome: ')))
    dados['nome'] = nome
    sexo = str(input(('Sexo: [ M/F ] '))).lower().strip()[0]
    dados['sexo'] = sexo
    if sexo == 'f':
        woman.append(nome)
    idade = int(input(('Idade: ')))
    dados['idade'] = idade
    soma_idade += idade
    pessoas.append(dados.copy())
    pergunta = str(input('Deseja adicionar mais ? [S/N]')).lower().strip()[0]
    if pergunta != 's':
        break
print(pessoas)
print('-=' * 30)
print(f'- O grupo tem {len(pessoas)} pessoas.')
media = soma_idade / len(pessoas)
print(f'- A Média de idade é de {media:.2f}.')
print('- As Mulheres cadastradas foram: ', end='')
for m in woman:
    print(f'{m} ', end='')
print()
print('- Lista das pessoas que estão acima da média:\n')
for pessoa in pessoas:
    if pessoa['idade'] > media:
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
        print()
print('-=' * 30)
print('<< ENCCERRADO >>')
