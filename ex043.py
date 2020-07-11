peso = float(input('Digite o seu Peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)
situação = ''
if imc < 18.5:
    situação = 'Abaixo do peso'
elif imc >= 18.5 and imc < 25:
    situação = 'Peso Ideal'
elif imc >= 25 and imc < 30:
    situação = 'Sobrepeso'
elif imc >= 30 and imc < 40:
    situação = 'Obesidade'
else:
    situação = 'Obesidade Mórbida'
print('O seu IMC atual equivale a : {:.1f} a sua situação no momento é {}'.format(imc, situação))
