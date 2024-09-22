#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dinheiro = float(input('Quantos reais e centavos você tem na carteira?'))

print('Com seus R${:.2f} você consegue comprar US${:.2f}!'.format(dinheiro, dinheiro / 5))