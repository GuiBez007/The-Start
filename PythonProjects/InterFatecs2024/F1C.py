# Alphabetic Pyramid

info = input()
info = info.split()

# check if the informed number is valid
if int(info[0]) < 1 or int(info[0]) > 26:
    exit()
else:
    abc = 'abcdefghijklmnopqrstuvwxyz'

    if info[1] == 'maiusculas':
        abc = abc.upper()

    abc_index = 0
    for i in range(25, -1, -1):
        if i == 25-int(info[0]):
            break

        print('.' * i, end='')
        print(abc[:abc_index+1])
        abc_index += 1
    # end of loop for