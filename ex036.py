print('$' * 70)
print('${}Izanagi Bank {}$'.format(' ' * 25, ' ' * 30))
print('$ Estamos aqui para quebrar as barreiras entre a ilusão e realidade. $')
print('$' * 70)
print('')

nome = str(input('Digite seu primeiro nome! '))
valorDaCasa = float(input('Qual o valor da casa ? '))
salario = float(input('Qual o valor do seu salário mensal ? '))
anos = int(input('Em quantos anos você pretende pagar ? '))
parcela = valorDaCasa / (anos * 12)
salario30 = salario * 30 / 100

if parcela <= salario30:
    print('Poderemos fazer negocios com o Sr.{}!'.format(nome))
    print(
        'O valor do imovel corresponde ao valor de R${} o valor da sua mensalidade a qual foi parcelado em {} vezes sera de R${:.2f} mensais'.format(
            valorDaCasa, anos * 12, parcela))
else:
    print(
        'Infelizmente no momento não poderemos aprovar o credito no valor de R${} para o Senhor(a) {}, mas nao se preocupe você poderar fazer uma nova verificação dentro de alguns meses!'.format(
            valorDaCasa, nome))
