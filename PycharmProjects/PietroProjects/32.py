#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = (input('Diga um ano qualquer: '))
bissexto = int(ano[-2:])

if bissexto % 4 == 0:
    print('{} é um ano Bissexto!'.format(ano))
else: print('{} não é um ano Bissexto.'.format(ano))