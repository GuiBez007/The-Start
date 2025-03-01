def inputVerification():
    while True:
        snakes_ladders = int(input())
        if 1 <= snakes_ladders <= 10:
            return snakes_ladders

def defineShortcuts(snakes_ladders):
    promotions_demotions = []
    for i in range(snakes_ladders):
        position = input().split()
        position[0] = int(position[0])
        position[1] = int(position[1])
        promotions_demotions.append(position)
    return promotions_demotions

def diceVerification():
    while True:
        dice_quantity = input()
        if 1 <= len(dice_quantity) <= 100:
            return dice_quantity.split()

def round(actual_pos, final_pos, dice, promo_demo, all_actual_pos):
    if len(all_actual_pos) == 0:
        print('Not affected')
    else:
        # chave
        for i in range(len(all_actual_pos)):
            count = 0
            # x representa cada atalho
            for x in promo_demo:
                if count == 0:
                    x[0], x[1] = x[1], x[0]
                    count = 1

                # pega o atalho
                if actual_pos == x[0]:
                    actual_pos = x[0]

                for z in dice:
                    actual_pos += int(z)

                if actual_pos == final_pos:
                    print()


def main():
    # número de atalhos a ser definidos
    snakes_ladders_quantity = inputVerification()
    # posição de todas as cobras e escadas em jogo
    promo_demo = defineShortcuts(snakes_ladders_quantity)
    # jogadas do dado
    dice = diceVerification()
    # posição final
    final_pos = int(input())
    ###
    actual_pos = 1
    all_actual_pos = []

    for i in dice:
        actual_pos += int(i)
        print(f'DADO -> {i}')
        print(f'actual pos -> {actual_pos}')
        for x in promo_demo:
            if actual_pos == x[0] or actual_pos == x[1]:
                all_actual_pos.append(actual_pos)

    round(1, final_pos, dice, promo_demo, all_actual_pos)

    print(actual_position)




main()

# DESISTI