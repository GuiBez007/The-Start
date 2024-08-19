#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

numero = int(input('Digite um número:'))

print('O DOBRO de {} vale {}. \nO TRIPLO vale {}. \nA RAÍZ QUADRADA de {} é igual a {}'
      .format(numero, numero * 2, numero * 3, numero, numero ** 0.5))