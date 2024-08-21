def showMatriz(m_1, m_2):
    for i in range(x):
        for j in range(y):




matriz_1 = 0
matriz_2 = 0

x_list = []
y_list = []

for z in range(2):
    print(f'Inform the {z+1}°matriz sizes')
    x = int(input('lines> '))
    y = int(input('columns> '))

    # matriz initialization
    for i in range(x):
        for j in range(y):
            x_list.append('   ')
        y_list.append(x_list[:])
        x_list.clear()
    if z == 0: matriz_1 = y_list[:]
    else: matriz_2 = y_list[:]


    # user entry
    for i in range(x):
        for j in range(y):
            showMatriz(matriz_1, matriz_2)
            if z == 0: matriz_1[i][j] = float(input('> '))
            else: matriz_2[i][j] = float(input('> '))

    x_list.clear()
    y_list.clear()

print(matriz_1)
print(matriz_2)