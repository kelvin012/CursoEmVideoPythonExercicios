total = 0
over_thousand = 0
cheapest = ''
cheapest_price = 0
c = 0
print('--' * 17)
print('{:º^34}'.format(' CAPITALISMO OPRESSOR '))
print('--' * 17)
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    total += preco
    if preco > 1000:
        over_thousand += 1

    if c != 1:
        cheapest = produto
        cheapest_price = preco
        c = 1
    elif preco < cheapest_price:
        cheapest = produto
        cheapest_price = preco

    pergunta = str(input('Deseja continuar? '))
    if pergunta != 's':
        break
print('{:º^34}'.format(' FIM DA LISTA '))
print(f'O valor total da compra foi de R${total}')
print(f'Temos {over_thousand} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {cheapest} que custa R${cheapest_price}')
