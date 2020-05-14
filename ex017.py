import math

num1 = float(input('Digite o comprimento do cateto oposto: '))
num2 = float(input('Digite o comprimento do cateto adjacente: '))
hipotenusa = math.hypot(num1, num2)
print('A hipotenusa do triangulo e equivalente a {:.2f}'.format(hipotenusa))
