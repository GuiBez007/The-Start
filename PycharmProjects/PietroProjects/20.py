#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')
alunos = [aluno1, aluno2, aluno3, aluno4]

shuffle(alunos)
print('A ordem é a seguinte: {}, {}, {}, {}'.format(alunos[0], alunos[1], alunos[2], alunos[3]))