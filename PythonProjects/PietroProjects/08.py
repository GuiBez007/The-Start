#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = float(input('Digite um número de medida em metros:'))

print('{} m equivale a {:.0f} cm. \n{:.0f} m é igual a {:.0f} mm.'
      .format(metro, metro * 100, metro, metro * 1000))



