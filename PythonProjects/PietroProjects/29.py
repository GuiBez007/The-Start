#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep

velocidade_carro = int(input('Qual a velocidade atual do seu carro? Km/h: '))

print("Hmmmmmm...");sleep(2)
if velocidade_carro > 80:                                                                    #←----CÁLCULO DA MULTA----→
    print('Você ultrapassou os 80Km/h! \nVai receber uma multa no valor de R${:.2f}!'.format((velocidade_carro - 80) * 7))
else: print('Pode passar.')