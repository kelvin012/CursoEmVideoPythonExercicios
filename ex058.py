from random import randint

pseudo_rng = randint(1, 10)
tentativas = 0
aposta = 0
while aposta != pseudo_rng:
    aposta = int(input('Digite um número > '))
    tentativas += 1
    if aposta != pseudo_rng:
        print('Você errou! Tente novamente :)')
print('PARABENS! Você acertou usando {} tentativa(s)'.format(tentativas))
