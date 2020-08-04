pessoas = list()
soma_idade = media = 0
while True:
    dados = dict()
    dados['nome'] = str(input('Nome: '))
    while True:
        sexo = str(input('Sexo: [ M/F ] ')).upper().strip()[0]
        if sexo in 'MF':
            break
        print('ERRO 404! Digite apenas um valor valido M ou F!')
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    soma_idade += dados['idade']
    pessoas.append(dados.copy())
    pergunta = str(input('Deseja adicionar mais ? [S/N]')).lower().strip()[0]
    if pergunta != 's':
        break
print('-=' * 30)
print(f'- O grupo tem {len(pessoas)} pessoas.')
media = soma_idade / len(pessoas)
print(f'- A Média de idade é de {media:.2f}.')
print('- As Mulheres cadastradas foram: ', end='')
for m in pessoas:
    if m['sexo'] == 'F':
        print(f'{m["nome"]} ', end='')
print()
print('- Lista das pessoas que estão acima da média:')
for pessoa in pessoas:
    if pessoa['idade'] > media:
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
        print()
print('-=' * 30)
print('<< ENCCERRADO >>')
