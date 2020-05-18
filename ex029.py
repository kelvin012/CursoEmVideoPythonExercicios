velocity = float(input('Digite a velocidade atual do seu veiculo: ').strip())
if velocity > 80:
    roubo = (velocity - 80) * 7
    print('PARABENS você excedeu o limite imoralmente imposto de 80km/h e foi multado!')
    print('Você foi roubado no valor de R${:.2f} que podera ser pago atraves do App do seu banco!'.format(roubo))
print('Tenha um bom dia, Dirija da forma que achar melhor!')
