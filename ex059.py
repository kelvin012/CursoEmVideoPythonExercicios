opcao = 0
control = 0
num1 = 0
num2 = 0
print('[1] Somar')
print('[2] Multiplicar')
print('[3] Maior número')
print('[4] Novos números')
print('[5] Sair do progama')
while opcao != 5:
    if control == 0:
        num1 = float(input('Digite um número : '))
        num2 = float(input('Digite outro número : '))
        control += 1
    print('=/' * 10)
    opcao = int(input('Escolha uma opção > '))
    print('=/' * 10)
    if opcao == 1:
        print('=-' * 30)
        print('O resultado da Soma dos numeros {} e {} é igual a > {}'.format(num1, num2, num1 + num2))
        print('=-' * 30)
    elif opcao == 2:
        print('=-' * 30)
        print('O resultado da Multiplicação do números {} e {} é igual a > {}'.format(num1, num2, num1 * num2))
        print('=-' * 30)
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print('=-' * 30)
        print('O Maior número é o -> {}'.format(maior))
        print('=-' * 30)
    elif opcao == 4:
        print('=-' * 30)
        num1 = float(input('Digite um número : '))
        num2 = float(input('Digite outro número : '))
        print('=-' * 30)
    elif opcao == 5:
        print('=-' * 30)
        print('Progama sendo encerrado!')
        print('=-' * 30)
    else:
        print('Opção Invalida!')
    control += 1
