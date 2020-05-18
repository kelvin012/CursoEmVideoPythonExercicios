from random import randint
from time import sleep

pseudoRandom = randint(1, 5)
print('--=' * 21)
print('Bip-Bop.....\nTente adivinhar o número que eu escolhi entre 1 e 5 -> ')
print('--=' * 21)
kick = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(2)
if kick == pseudoRandom:
    print('PARABENS você chutou {} e este foi o numero gerado pseudo-aleatoriamente pelo computador!'.format(kick))
else:
    print('QUE PENA você deixou a futura SKY-NET ganhar! Seu chute foi {} e numero gerado era {}'.format(kick, pseudoRandom))
