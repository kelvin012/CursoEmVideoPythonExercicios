from datetime import date

nascimento = int(input('Digite o Ano do seu nascimento! '))
anoAtual = date.today().year
idade = anoAtual - nascimento
categoria = ''
if idade <= 9:
    categoria = 'MIRIN'
elif idade > 9 and idade <= 14:
    categoria = 'INFANTIL'
elif idade > 14 and idade <= 19:
    categoria = 'JUNIOR'
elif idade > 19 and idade <= 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print('A sua idade é : {}\nE você se encaixa na categoria de natação -> {}'.format(idade, categoria))
