c = 0
while True:
    n = int(input('Quer mostrar a tabuada de qual número ? '))
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c} = {n * c}')
        c += 1
    c = 0
print('Execução do progama finalizada!')
