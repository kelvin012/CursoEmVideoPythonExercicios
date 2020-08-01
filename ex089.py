alunos = []

while True:
    aluno = []
    notas = []
    nome = str(input('Nome: '))
    for i in range(1, 3):
        nota = float(input(f'Nota {i}: '))
        notas.append(nota)
    media = (notas[0] + notas[1]) / 2
    aluno.append(nome)
    aluno.append(notas)
    aluno.append(media)
    alunos.append(aluno[:])
    aluno.clear()
    pergunta = str(input('Deseja adicionar mais? ')).strip().lower()[0]
    if pergunta != 's':
        break
print('-=' * 25)
print('No. NOME           MÉDIA')
print('--' * 15)
for i in range(0, len(alunos)):
    print(f'{i}   {alunos[i][0]:<15} {alunos[i][2]:.1f}')
print('--' * 15)
while True:
    pergunta = int(input('Mostrar Notas de qual aluno? [999 to EXIT] '))
    if pergunta == 999:
        break
    else:
        print('--' * 15)
        if 0 <= pergunta <= len(alunos) - 1:
            print(f'Notas de {alunos[pergunta][0]} são {alunos[pergunta][1]}')
        else:
            print('Aluno inexistente!')
        print('--' * 15)
print('FINALIZANDO...')
print('<<< VOLTE SEMPRE >>>')
