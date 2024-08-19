# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Qual o valor da casa? '))
salario = float(input('Seu salário? ')) / 100 * 30
meses = int(input('Em quantos anos você você paga? ')) * 12

prestacao = casa / meses
print(salario)
if prestacao > salario:
    print('A prestação seria de R${:.2f} \nEmpréstimo negado!'.format(prestacao))
else:
    print('A prestação será de R${:.2f} \nEmpréstimo aceito!'.format(prestacao))