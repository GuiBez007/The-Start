from os import system

class Matriz:
    count = 0

    def __init__(self):
        Matriz.count += 1
        self.count = Matriz.count
        self.x = int(input('LINHAS> '))
        self.y = int(input('COLUNAS> '))
        self.values = self.matrizInicialization()
        self.addValues()


    def matrizInicialization(self):
        x_list = []
        y_list = []
        for i in range(self.x):
            for j in range(self.y):
                y_list.append(' ')
            x_list.append(y_list[:])
            y_list.clear()
        return x_list[:]


    def addValues(self):
        for i in range(self.x):
            for j in range(self.y):
                system('cls')
                self.showMatriz()
                self.values[i][j] = int(input('> '))
        system('cls')
        self.showMatriz()
        system('cls')


    def showMatriz(self):
        print('='*(self.y) + f' Matriz {self.count} ' + '='*(self.y))
        for i in range(self.x):
            print(' [', end='')
            for j in range(self.y):
                if j == self.y-1:
                    break
                print(f'{self.values[i][j]:3}', end=',')
            print(f'{self.values[i][j]:3}', end=']\n')


    def showAll(self, m_1, m_2, m_3, operation):
        _max = max(m_1.x, m_2.x, m_3.x)
        aux = len(str(m_1.values[0]))
        print(f'{'=== Matriz 1 ===':^{aux}}    {operation}    {'=== Matriz 2 ===':^{aux}}    =    {'=== Matriz 3 ===':^{aux}}')
        for i in range(_max):
            print(f'{str(m_1.values[i]):^16}         {str(m_2.values[i]):^16}         {str(m_3.values[i]):^16}')

########################################################################################

def sumOrSubtract(operation, m_1, m_2):
    m_3 = []
    aux = []
    for i in range(m_1.x):
        for j in range(m_1.y):
            if operation == '+':
                aux.append(m_1.values[i][j] + m_2.values[i][j])
            else:
                aux.append(m_1.values[i][j] - m_2.values[i][j])
        m_3.append(aux[:])
        aux.clear()
    return m_3


def multiplyMatrix(m_1, m_2):
    if m_1.y != m_2.x:
        print('ERROR!') # arrumar dps

    m_3 = []
    aux = []
    for line_m1 in range(m_1.x):
        for column_m2 in range(m_2.y):
            _sum = 0
            for key in range(m_2.x):
                _sum += m_1.values[line_m1][key] * m_2.values[key][column_m2]
            aux.append(_sum)
        m_3.append(aux[:])
        aux.clear()
    return m_3



def resultOfOperation(m_3):
    system('cls')
    print('RESULTADO')
    aux = m_3[:]
    m_3 = Matriz.__new__(Matriz)
    m_3.values = aux[:]
    m_3.y = len(m_3.values[0])
    m_3.x = len(m_3.values)
    if Matriz.count != 3:
        Matriz.count += 1
    m_3.count = Matriz.count
    return m_3


def main():
    matriz_1 = Matriz()
    matriz_2 = Matriz()

    while True:
        print('\n=== CALCULOS DE MATRIZES === \n'
              '[01] - para somar;             \n'
              '[02] - para subtrair;          \n'
              '[03] - para multiplicar;       \n'
              '[04] - para dividir;           \n'
              '[05] - sair.                    ')
        option = int(input('opção> '))

        if option == 1:
            matriz_3 = sumOrSubtract('+', matriz_1, matriz_2)
            matriz_3 = resultOfOperation(matriz_3)
            Matriz.showAll(0,matriz_1, matriz_2, matriz_3, '+')
        elif option == 2:
            matriz_3 = sumOrSubtract('-', matriz_1, matriz_2)
            matriz_3 = resultOfOperation(matriz_3)
            Matriz.showAll(0, matriz_1, matriz_2, matriz_3, '-')
        elif option == 3:
            matriz_3 = multiplyMatrix(matriz_1, matriz_2)
            matriz_3 = resultOfOperation(matriz_3)
            matriz_3.showMatriz() # tenho que arrumar para mostrar tudo
        elif option == 4:
            pass
        elif option == 5:
            break


if __name__ == '__main__':
    main()