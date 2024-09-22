#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Digite um número: ')) % 2
            #↓---RESTO DA DIVISÃO
if numero == 0:
    print('Seu número é Par!')
else: print('Seu número é Ímpar!')
