from random import choice

def initialPosition(moves):
    position = []
    while len(position) < 2:
        aux = choice(moves)
        if aux not in position:
            position.append(aux)
    return position

def numberVerification():
    while True:
        number = int(input())
        if 1 <= number <= 80:
            return number

def main():
    moves = ['up', 'down', 'left', 'right']
    legs_moved = 0
    leg = 0
    legs_position = initialPosition(moves)

    for i in range(numberVerification()):
        instruction = input()
        if instruction not in legs_position:
            legs_moved += 1
            legs_position[leg] = instruction

            if leg == 0:
                leg = 1
            else:
                leg = 0
    print(legs_moved)


main()