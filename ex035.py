reta1 = float(input('Digite o tamanho da reta 1: '))
reta2 = float(input('Digite o tamanho da reta 2: '))
reta3 = float(input('Digite o tamanho da reta 3: '))

if reta1 + reta2 > reta3:
    print('Os segmentos de reta {},{},{} podem sim formar um triangulo!'.format(reta1, reta2, reta3))
else:
    print('Os segmentos de reta {},{},{} não podem formar um triangulo!'.format(reta1, reta2, reta3))
