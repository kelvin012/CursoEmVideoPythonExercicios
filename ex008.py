metros = float(input('Digite uma quantidade em metros para ser convertida! '))
milimetros = metros * 1000
centimetros = metros * 100
dm = metros * 10
dam = metros * 0.1
hm = metros * 0.01
km = metros * 0.001

print('{} metros convertidos para milimetros e igual a {:.0f} milimetros'.format(metros, milimetros))
print('{} metros convertidos para centimetros e igual a {:.0f} centimetros'.format(metros, centimetros))
print('{} metros convertidos para dm e igual a {:.0f}'.format(metros,dm))
print('{} metros convertidos para dam e igual a {}'.format(metros,dam))
print('{} metros convertidos para hm e igual a {}'.format(metros,hm))
print('{} metros convertidos para km e igual a {}'.format(metros,km))
