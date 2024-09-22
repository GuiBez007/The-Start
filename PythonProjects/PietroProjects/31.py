#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

distancia_viagem = int(input('Qual a distância da sua viagem? Km: '))

if distancia_viagem <= 200:
    print('Viagem pequena demais! Você será cobrado R$0,05 a mais por cada km percorrido. \nVocê deverá pagar R${:.2f} pela viagem.'.format(distancia_viagem * 0.50))
else: print('Você deverá pagar R${:.2f} pela viagem.'.format(distancia_viagem * 0.45))