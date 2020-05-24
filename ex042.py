print('--=' * 12)
print('Analisador de Triângulos v2.0')
print('--=' * 12)

l1 = float(input('Digite o tamanho da reta 1: '))
l2 = float(input('Digite o tamanho da reta 2: '))
l3 = float(input('Digite o tamanho da reta 3: '))
categoria = ''

if (l1 + l2 > l3 and l2 + l3 > l1 and l1 + l3 > l2):
    if l1 == l2 and l1 == l3:
        categoria = 'Equilátero'
    elif l1 == l2 or l1 == l2 or l2 == l3:
        categoria = 'Isósceles'
    else:
        categoria = 'Escaleno'
    print('Os segmentos de reta {}, {}, {} podem formar um Triangulo do tipo: {}.'.format(l1, l2, l3, categoria))
else:
    print('Os segmentos de reta {}, {}, {} não podem formar um Triangulo!'.format(l1, l2, l3))
