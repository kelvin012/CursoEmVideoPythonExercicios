def area(lar, com):
    out = lar * com
    print(f'A área dde um terreno {lar:.1f}x{com:.1f} é de {out}m².')


print('Medidor de Terrenos!')
print('--' * 15)
largura = float(input('LARGURA(m): '))
comprimento = float(input('COMPRIMENTO(m): '))
area(largura, comprimento)
