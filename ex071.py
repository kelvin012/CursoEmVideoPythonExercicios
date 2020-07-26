print('--' * 25)
print('{}{:^48}{}'.format('|', ' BANCO IZANAGI', '|'))
print('--' * 25)
saque = int(input('Qual valor sera sacado? R$'))
c50 = 0
c20 = 0
c10 = 0
c1 = 0
while True:
    if saque >= 50:
        saque -= 50
        c50 += 1
    elif saque >= 20:
        saque -= 20
        c20 += 1
    elif saque >= 10:
        saque -= 10
        c10 += 1
    elif saque <= 9 and saque > 0:
        saque -= 1
        c1 += 1
    elif saque == 0:
        break

print('{}{:^48}{}'.format('|', str(c50) + ' nota(s) de R$ 50,00', '|'))
print('{}{:^48}{}'.format('|', str(c20) + ' nota(s) de R$ 20,00', '|'))
print('{}{:^48}{}'.format('|', str(c10) + ' nota(s) de R$ 10,00', '|'))
print('{}{:^48}{}'.format('|', str(c1) + ' nota(s) de R$ 1,00', '|'))
print('--' * 25)

'''        
print('{} nota(s) de R$ 50,00'.format(c50))
print('{} nota(s) de R$ 20,00'.format(c20))
print('{} nota(s) de R$ 10,00'.format(c10))
print('{} nota(s) de R$ 1,00'.format(c1))
'''
