#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input('Diga uma temperatura em °C: '))
fahrenheit = celsius * 1.8 + 32

print('A temperatura de {}°C convertida em °F se torna {}°F!'.format(celsius, fahrenheit))
