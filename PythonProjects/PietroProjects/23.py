#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input())
print('uni {} \ndez {} \ncen {} \nmil {}'
      .format((numero) % 10, (numero // 10) % 10, (numero // 100) % 10, (numero // 1000) % 10))
