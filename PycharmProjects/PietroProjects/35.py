#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = int(input('Digite o comprimento da primeira reta: '))
reta2 = int(input('Digite o comprimento da segunda reta: '))
reta3 = int(input('Agora digite o comprimento da última reta: '))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta3 + reta1 > reta2:
    print('Essas retas podem formar um triângulo!')
else:
    print('Essas retas não podem formar umn triângulo.')