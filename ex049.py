tabuada = int(input('Digite um número: '))

j = 0
for i in range(0, 10):
    print('{} X {} = {}'.format(tabuada, j, tabuada * (i + 1)))
    j += 1
