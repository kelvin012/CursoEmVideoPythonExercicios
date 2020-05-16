from random import randint

pseudoRandom = randint(1, 5)
kick = int(input('Digite um número entre 1 e 5 -> '))
if kick == pseudoRandom:
    print('PARABENS você chutou {} e este foi o numero gerado pseudo-aleatoriamente pelo computador!'.format(kick))
else:
    print('QUE PENA você deixou a futura SKY-NET ganhar! Seu chute foi {} e numero gerado era {}'.format(kick,
                                                                                                         pseudoRandom))
