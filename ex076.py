lista_compras = ('lapis', 1.19, 'caderno', 22.99, 'borraacha', 0.50,
                 'lapiseira', 2.50, 'notebook', 1259.99, 'Mochila', 122.59)

print('--' * 25)
print('{:^50}'.format('LISTAGEM DE PREÇOS'))
print('--' * 25)
for index in range(0, len(lista_compras), 2):
    nome = lista_compras[index]
    preco = lista_compras[index + 1]
    print(f'{nome:.<40}', end='')
    print(f'R${preco:>8.2f}')
print('--' * 25)
