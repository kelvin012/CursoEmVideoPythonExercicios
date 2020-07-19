frase = str(input('Digite uma frase que sera embaraçada > ')).lower().replace(' ', '')
#frase_invertida = frase[::-1]
frase_invertida = ''
for i in reversed(frase):
    frase_invertida += i
if frase == frase_invertida:
    print('A frase {} quando invertida vale {} e como ambas são iguais elas são chamadas de Palíndromas!'.format(frase, frase_invertida))
else:
    print('A frase {} quando invertida vale {} e são diferentes!'.format(frase, frase_invertida))
