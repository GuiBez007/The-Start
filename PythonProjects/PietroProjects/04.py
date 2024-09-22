#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

digito = input('Escreva qualquer coisa:')
resposta = 'Este valor' #TEXTO PARA SER REPETIDO EM TODA INCRÍVEL FRASE

print('O tipo primitivo deste valor é:', type(digito))
print(resposta,'só tem espaços?', digito.isspace())
print(resposta,'é um número?', digito.isnumeric())
print(resposta,'é alfabético?', digito.isalpha())
print(resposta,'é alfanumérico?', digito.isalnum())
print(resposta,'está apenas em minúsculas?', digito.islower())
print(resposta,'está apenas em maiúsculas?', digito.isupper())
print(resposta,'têm a letra inicial maiúscula?', digito.istitle())




