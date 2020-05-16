velocity = float(input('Digite a velocidade atual do seu veiculo: '))
if velocity > 80:
    multa = (velocity - 80) * 7
    print('PARABENS você acaba de seu roubado no valor de R${:.2f} que podera ser paga atraves do app do seu banco!'.format(multa))
