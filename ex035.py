print('--=' * 12)
print('Analisador de Triângulos v1.0')
print('--=' * 12)
l1 = float(input('Digite o tamanho da reta 1: '))
l2 = float(input('Digite o tamanho da reta 2: '))
l3 = float(input('Digite o tamanho da reta 3: '))
t1 = False
t2 = False
t3 = False
if l1 + l2 > l3:
    t1 = True
if l2 + l3 > l1:
    t2 = True
if l1 + l3 > l2:
    t3 = True
if t1 and t2 and t3 == True:
    print('Os segmentos de reta {},{},{} podem sim formar um triangulo!'.format(l1, l2, l3))
else:
    print('Os segmentos de reta {},{},{} não podem formar um triangulo!'.format(l1, l2, l3))
