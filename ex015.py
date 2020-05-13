km = float(input('Quantos kilometros você rodou com o carro ? '))
diasAlugado = int(input('Quantos dias você ficou com o carro ?'))
valorKmRodado = km * 0.15
valorDiasAlugado = diasAlugado * 60
valorTotal = valorKmRodado + valorDiasAlugado
print('O valor proporcional a {} dias alugados equivale a R${:.2f} e custo por rodar {}Km e igual a R${:.2f} portanto o valor total a ser pago sera de R${:.2f}'.format(diasAlugado, valorDiasAlugado, km, valorKmRodado, valorTotal))
