#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nota1_aluno = float(input('Primeira nota do aluno:'))
nota2_aluno = float(input('Segunda nota do aluno:'))

print('A média entre os números {} e {} é igual a {:.1f}'
      .format(nota1_aluno, nota2_aluno, (nota1_aluno + nota2_aluno) / 2))
