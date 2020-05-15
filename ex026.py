frase = input('Digite uma frase qualquer: ')
print('A letra \"A\" apareceu {} vezes '.format(frase.upper().count('A')))
print('A letra \"A\" aparece pela primeira vez no indice {}'.format(frase.upper().find('A')))
print('A letra \"A\" aparece pela ultima vez no indice {}'.format(frase.upper().rfind('A')))
