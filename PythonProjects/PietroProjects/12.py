#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Digite o valor em R$ de um produto:'))
desconto = produto / 100 * 5

print('Seu produto vale R${:.2f} certo? \nCom um desconto de 5%, ele passaria a valer R${:.2f}!'.format(produto, produto - desconto))