a1 = int(input('Digite o primeiro termo da progessão: '))
r = int(input('Digite a Razão da progressão: '))
t = a1
c = 1
while c <= 10:
    print('{}'.format(t), end=' -> ')
    t += r
    c += 1
print('FIM')
