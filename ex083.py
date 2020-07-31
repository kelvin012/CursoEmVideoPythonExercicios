expressao = str(input('Digite a expressão: '))
pilha = []
for caractere in expressao:
    if caractere == '(':
        pilha.append('(')
    elif caractere == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expresão está válida!')
else:
    print('Sua expressão esta errada!')
