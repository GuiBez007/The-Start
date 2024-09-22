#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome_pessoa = str(input('Digite seu nome completo: ')).strip().split()

print('O primeiro nome é: {} \nE o último nome é: {}'.format(nome_pessoa[0], nome_pessoa[-1]))