def notas(*grades, sit=False):
    """
    -> Função para analisar notas e sítuações de vários alunos.
    :param grades: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação da turma.
    :return: dicionário com varías informaçoes sobre a situação da turma.
    """

    turma = dict()
    index = maior = menor = somatorio = 0
    for grade in grades:
        somatorio += grade
        if index == 0:
            maior = menor = grade
            index += 1
        else:
            if grade > maior:
                maior = grade
            if grade < menor:
                menor = grade
    turma['total'] = len(grades)
    turma['maior'] = maior
    turma['menor'] = menor
    turma['média'] = somatorio / turma['total']
    if sit:
        if turma['média'] > 7:
            turma['situação'] = 'BOA'
        elif 7 > turma['média'] >= 6:
            turma['situação'] = 'RAZOÁVEL'
        elif 6 > turma['média'] >= 4:
            turma['situação'] = 'RUIM'
        elif 4 > turma['média']:
            turma['situação'] = 'PESSIMA'
    return turma


resposta = notas(3.5, 5, 6.5, 2, 2.9, sit=True)
print('--' * 15)
print(resposta)
# help(notas)
