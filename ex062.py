print('Gerador de Progessão Aritmética!')
print('=-' * 17)
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a Razão da PA: '))
t = a1
c = 1
total = 0
pergunta = 10
while pergunta != 0:
    total = total + pergunta
    while c <= total:
        print('{}'.format(t), end=' -> ')
        t += r
        c += 1
    print('PAUSA')
    pergunta = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão Aritmética finalizada com {} termos exibidos.'.format(total))
