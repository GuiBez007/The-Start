#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
numero3 = int(input('Digite mais um número: '))

#DEFINIR QUAL NÚMERO DIGITADO É O → MAIOR ←
if numero1 > numero2 and numero1 > numero3:
    numero_maior = numero1
if numero2 > numero3 and numero2 > numero1:
    numero_maior = numero2
if numero3 > numero1 and numero3 > numero2:
    numero_maior = numero3

#DEFINIR QUAL NÚMERO DIGITADO É O → MENOR ←
if numero1 < numero2 and numero1 < numero3:
    numero_menor = numero1
if numero2 < numero3 and numero2 < numero1:
    numero_menor = numero2
if numero3 < numero1 and numero3 < numero2:
    numero_menor = numero3

print('O MAIOR número digitado foi o {}. \nE o MENOR número digitado foi o {}.'.format(numero_maior, numero_menor))





