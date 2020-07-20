num = int(input('Digite um número: '))
F1 = 0
F2 = 1
print('0 -> ', end='')
while num > 0:
    Fn = F1 + F2
    F1 = F2
    F2 = Fn
    print(Fn, end=' -> ')
    num -= 1
print('FIM')
