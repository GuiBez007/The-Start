#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nome_cidade = input('Diga o nome de uma cidade:').strip()

print('{}!'.format(nome_cidade.upper()[:5] == 'SANTO'))

