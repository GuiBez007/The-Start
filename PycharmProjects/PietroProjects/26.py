#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”,
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).upper().strip()
tamanho = len(frase)

print('A letra “A” apareceu {} vezes na frase; \nA primeira vez na posição {} e por último na posição {}'
      .format(frase.count('A'), frase.find('A') + 1, tamanho - frase[::-1].find('A')))