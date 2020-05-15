nome = str(input('Digite seu nome : ')).strip()
separado = nome.split()
print('Seu primeiro nome é {}'.format(separado[0]))
print('Seu último nome é {}'.format(separado[-1]))
