a1 = int(input('Digite o primeiro termo da progessão: '))
r = int(input('Digite a Razão da progressão: '))

for n in range(0, 10):
    An = a1 + ((n + 1) - 1) * r
    print(An)
