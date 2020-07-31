expressao = str(input('Digite a expressão: '))
parentenses = list()
resultado = list()

for caractere in expressao:
    if caractere == '(' or caractere == ')':
        parentenses.append(caractere)
# print(parentenses)
invertido = sorted(parentenses, reverse=True)
# print(invertido)
for i in range(0, len(parentenses)):
    if (parentenses[i] == '(' and invertido[i] == ')') or (parentenses[i] == ')' and invertido[i] == '('):
        resultado.append(1)
    else:
        resultado.append(0)
if 0 not in resultado:
    print('Sua expresão está válida!')
else:
    print('Sua expressão esta errada!')
