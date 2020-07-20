a1 = int(input('Digite o primeiro termo da progessão: '))
r = int(input('Digite a Razão da progressão: '))
decimo = a1 + (10 - 1) * r

'''c = 1

while c < 11:
    An = a1 + ((c) - 1) * r
    print('{}'.format(An), end=' -> ')
    c += 1
print('FIM!')
'''
c = 0
while c < 10:
    An = a1 + (c - 1) * r
    print('{}'.format(An + r), end=' -> ')
    c += 1
print('FIM')
