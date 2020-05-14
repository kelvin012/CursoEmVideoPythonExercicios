from math import radians,sin,cos,tan

angulo = float(input('Digite o valor do ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O Ângulo {} tem como Seno {:.2f}, Cosseno {:.2f},Tangente {:.2f}'.format(angulo, seno, cosseno, tangente))
