#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Quanto você ganha com seu salário? '))

if salario > 1250:
    aumento = salario + salario / 100 * 10
if salario <= 1250:
    aumento = salario + salario / 100 * 15

print('Com o aumento, seu novo salário será de R${:.2f}!'.format(aumento))