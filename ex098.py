from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    print(f'Contagem de {inicio} até {fim} de {abs(passo)} em {abs(passo)}')
    sleep(1)
    if inicio < fim:
        for num in range(inicio, fim + 1, abs(passo)):
            sleep(0.3)
            print(f'{num} ', end='', flush=True)
        print('FIM!')
    elif inicio > fim:
        for num in range(inicio, fim - 1, -abs(passo)):
            sleep(0.3)
            print(f'{num} ', end='', flush=True)
        print('FIM!')


print('-=' * 15)
contador(1, 10, 1)
print('-=' * 15)
contador(10, 0, 2)
print('-=' * 15)
print('Como você quer fazer a contagem ?')
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))
print('-=' * 15)
