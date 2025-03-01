





def main():
    sticks = int(input())
    pos = []

    for i in range(sticks):
        position = input().split()
        initial = ' '.join(position[:2])
        final = ' '.join(position[2:])
        position.clear()
        position.append(initial[:])




        while position[-1][0] < final[0]:
            position.append(position[-1].replace(position[-1][0], str(int(position[-1][0])+1)))
            print(position)

        pos.append(position)






main()