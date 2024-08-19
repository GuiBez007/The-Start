#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

catetoposto = float(input('Digite o valor do cateto oposto: '))
catetoadjacente = float(input('Agora digite o valor do cateto adjacente: '))
hipotenusa = catetoposto ** 2 + catetoadjacente ** 2

print('O valor da hipotenusa é de {:.2f}!'.format(hipotenusa ** 0.5))
