salario = float(input('Digite o valor do seu salario R$ '))
if (salario > 1250):
    aumento = ((salario * 10) / 100)
    salario = salario + aumento
    print(
        'O valor do seu salario reajustado sera de R${} o qual representa um aumento de R${}'.format(salario, aumento))
else:
    aumento = ((salario * 15) / 100)
    salario = salario + aumento
    print(
        'O valor do seu salario reajustado sera de R${} o qual representa um aumento de R${}'.format(salario, aumento))
