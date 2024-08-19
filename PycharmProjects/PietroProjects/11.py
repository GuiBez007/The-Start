#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Diga a LARGURA da parede em metros:'))
altura = float(input('Agora diga a ALTURA da parede, também em metros:'))
area = largura * altura

print('Dadas as dimenções {} x {}, A área total da parede é igual a {}m².'
      '\nSeriam necessários {} litros de tinta para pintá-la totalmente.'
      .format(largura, altura, area, area / 2))


