#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Diga o seu atual salário, em R$:'))
aumento = salario / 100 * 15

print('Com seu atual salário de R${:.2f}, um aumento de 15% o deixaria com um novo salário de R${:.2f}!'.format(salario, salario + aumento))