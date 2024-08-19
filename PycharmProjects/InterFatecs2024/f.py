# Simplificando a Geometria

values = []
num = '0123456789.'
while True:
    info = input()

    if info[0] == '0' and info[2] == '0' and info[4] == '0':
        break

    splited_info = info.split()
    a = int(splited_info[0])
    b = int(splited_info[1])
    c = int(splited_info[2])

    if c == -1:
        c = a**2 + b**2
        lenght = c**0.5

        if str(lenght) not in num: '5.000' ##
            print('Impossible.')
        show = 'c = {:.3f}'.format(lenght)
        values.append(show)
    elif b == -1:
        b = c**2 - a**2
        lenght = b**0.5

        if str(lenght) not in num:
            print('Impossible.')
        show = 'b = {:.3f}'.format(lenght)
        values.append(show)
    elif a == -1:
        a = c**2 - b**2
        lenght = a**0.5

        if str(lenght) not in num:
            print('Impossible.')
        show = 'a = {:.3f}'.format(lenght)
        values.append(show)

for i in range(len(values)):
    print('Triangle #{}'.format(i+1))
    print('{} type{}'.format(values[i]))
