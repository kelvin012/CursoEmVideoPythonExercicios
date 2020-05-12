altura = float(input('Qual a altura da parede ? '))
largura = float(input('Qual é a largura da parede ? '))
area = altura * largura
qtdLitrosTinta = area / 2
print(
    'A area da sua parede de {} de altura por {} de largura equivale a {} metros quadrados, considerando essa parede você ira precisar de {} Litros de tinta para pintar completamente a sua parede!'.format(
        altura, largura, area, qtdLitrosTinta))
