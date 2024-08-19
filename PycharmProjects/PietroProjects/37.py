# Escreva um programa em Python que leia um número inteiro qualquer e
# peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

print('               Conversor de Bases Numéricas               \n')

numero = int(input('Digite um número: '))
base = int(input('''Para qual base você quer converter este número? Digite:\n
[1] para binário;
[2] para octal;
[3] para hexadecimal.\n
→ '''))

if base == 1:
    convertido = bin(numero)
    nome = 'binário'
elif base == 2:
    convertido = oct(numero)
    nome = 'octal'
elif base == 3:
    convertido = hex(numero)
    nome = 'hexadecimal'
print('{} Convertido em {}:\n→ {}'.format(numero, nome, convertido[2:]))