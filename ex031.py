distancia = float(input('Digite a distancia em Km da sua viagem: '))
if distancia <= 200:
    valor = distancia * 0.50
    print('O valor da sua viagem foi de R${:.2f}'.format(valor))
else:
    valor = distancia * 0.45
    print('O valor da sua viagem foi de R${:.2f}'.format(valor))
print('OBRIGADO por utilizar nossos serviços estamos sempre ao seu dispor!')
