#Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

nome_pessoa = input('Escreva seu nome completo: ')
nome_pessoa = nome_pessoa.strip()

numero_de_letras = len(nome_pessoa)
n_espaços = nome_pessoa.count(' ')
lista = nome_pessoa.split()

print('Aqui está seu nome em maiúsculas: {}'.format(nome_pessoa.upper()))
print('Aqui está seu nome em minúsculas: {}'.format(nome_pessoa.lower()))

print('A quantidade total de letras do seu nome: {}'.format(numero_de_letras - n_espaços))
print('O seu primeiro nome tem um total de {} letras.'.format(len(lista[0])))