number = int(input('Digite um numero entre 0 e 9999 : '))
unidade = number // 1 % 10
dezena = number // 10 % 10
centena = number // 100 % 10
milhar = number // 1000 % 10
print('unidade: {}\ndezena: {}\ncentena: {}\nmilhar: {}'.format(unidade, dezena, centena, milhar))
