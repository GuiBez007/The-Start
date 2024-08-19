#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5
#peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint

numero = int(input('Pense e digite um número Inteiro entre 0 e 5: '))
pensar = randint(0, 5)

print('O número escolhido era {}!' .format(pensar))

if numero == pensar:
    print('Você acertou! :)')
else:
    print('você está errado usuário')
