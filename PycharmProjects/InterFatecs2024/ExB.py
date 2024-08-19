# Balas Dumbinho

candy_code = input()
SUM = 0

# limita o código da bala de 0 a 1000000
if 0 < int(candy_code) <= 1000000:

    # faz a soma dos números do código
    for num in candy_code:
        SUM += int(num)

    # checa se par ou ímpar e mostra resultado
    if SUM % 2 == 0:
        print('dumbinho')
    else:
        print('8-bonito')
