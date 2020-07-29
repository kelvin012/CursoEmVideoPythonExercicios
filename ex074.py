from random import randint

a = 1
b = 10
cinco_rng = (randint(a, b), randint(a, b), randint(a, b), randint(a, b), randint(a, b))

print('Os valores sorteados foram: ', end='')
for pos, i in enumerate(cinco_rng):
    if pos != len(cinco_rng) - 1:
        print(i, end=', ')
    else:
        print(i)
print(f'O maior número sorteado foi {max(cinco_rng)}')
print(f'O menor número sorteado foi {min(cinco_rng)}')
