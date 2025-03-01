def numberVerification():
    while True:
        number = int(input())
        if 1 <= number <= 80:
            return number

def main():
    switched = False
    legs_moved = 0
    leg = 0
    legs_position = []

    for i in range(numberVerification()):
        instruction = input()
        if switched == False:
            if leg == 1: leg = 0
            else: leg = 1

        if i == 0 or i == 1:
            legs_position.append(instruction)
        else:
            if instruction != legs_position[0] and instruction != legs_position[1]:
                switched = True
                legs_position[leg] = instruction
                legs_moved += 1

                if leg == 0:
                    leg = 1
                else:
                    leg = 0

    print(legs_moved)


main()