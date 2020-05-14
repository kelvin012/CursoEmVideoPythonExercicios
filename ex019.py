from random import randint

aluno1 = str(input('Digite o nome do aluno 1 '))
aluno2 = str(input('Digite o nome do aluno 2 '))
aluno3 = str(input('Digite o nome do aluno 3 '))
aluno4 = str(input('Digite o nome do aluno 4 '))
lista = [aluno1, aluno2, aluno3, aluno4]
sorteado = randint(1, len(lista))
print('O felizardo que foi escolhido pseudo-aleatoriamente foi o aluno {}'.format(lista[sorteado]))
