nota1 = float(input('Digite a sua primeira nota: '))
nota2 = float(input('Digite a sua segunda nota: '))
media = (nota1 + nota2) / 2

if media < 5:
    print('Sua MEDIA foi de {} e você esta REPROVADO!'.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua MEDIA foi de {} e você tera que fazer uma prova de RECUPERAÇÃO!'.format(media))
elif media > 7:
    print('PARABENS sua MEDIA foi de {} e você foi APROVADO!'.format(media))
