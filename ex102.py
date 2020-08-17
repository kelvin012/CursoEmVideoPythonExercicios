def fatorial(n=1, show=False):
    """
    -> Faz uma contagem e mostra na tela
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        # print(c)
        if show:
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c}', end='')
            if c == 1:
                print(f' = {f}')
        f *= c
    if not show:
        return f
    else:
        return ''


print('--' * 15)
print(fatorial(5, True))
# help(fatorial)
