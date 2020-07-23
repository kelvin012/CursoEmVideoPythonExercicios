from random import randint

pseudo_rng = randint(1, 10)
tentativas = 0
aposta = 0
print('Bip Bop! Pensei em um número que esta contido entre 1 e 10!')
print('Será se você pode adivinhar ?')
while aposta != pseudo_rng:
    aposta = int(input('Digite um número > '))
    tentativas += 1
    if aposta > pseudo_rng:
        print('Você errou! Tente novamente com um número Menor :)')
    elif aposta < pseudo_rng:
        print('Você errou! Tente novamente com um número Maior :)')
print('PARABENS! Você acertou usando {} tentativa(s)'.format(tentativas))
