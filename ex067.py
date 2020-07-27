while True:
    n = int(input('Quer mostrar a tabuada de qual número ? '))
    print('--' * 22)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('--' * 22)
print('Execução do progama finalizada!')
