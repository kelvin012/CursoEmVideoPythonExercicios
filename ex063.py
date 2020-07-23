num = int(input('Quantos Termos serão mostrados? '))
F1 = 0
F2 = 1
C = 3
print('{} -> {} -> '.format(F1, F2), end='')
while C <= num:
    Fn = F1 + F2
    F1 = F2
    F2 = Fn
    print(Fn, end=' -> ')
    C += 1
print('FIM')
