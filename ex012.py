preco = float(input('Qual o preço do produto ? R$'))
desconto = 5
valorComDesconto = preco - ((desconto * preco) / 100)
print('O valor final do produto com o desconto de {:.2f}% da liquidação é {:.2f}'.format(desconto ,valorComDesconto))
