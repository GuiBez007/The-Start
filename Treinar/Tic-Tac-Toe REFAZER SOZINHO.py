#Name: Tic-Tac-Toe
#Author: GUilherme Bezerra
#Date: 26/05/2023 15:44
#Description: ...jogo da velha ☺

def display_board(board):
    print ("+-------+-------+-------+\n|       |       |       |\n|  ",board[0][0],"  |  ",board[0][1],"  |  ",board[0][2],"  |\n|       |       |       |")
    print ("+-------+-------+-------+\n|       |       |       |\n|  ",board[1][0],"  |  ",board[1][1],"  |  ",board[1][2],"  |\n|       |       |       |")
    print ("+-------+-------+-------+\n|       |       |       |\n|  ",board[2][0],"  |  ",board[2][1],"  |  ",board[2][2],"  |\n|       |       |       |")
    print ("+-------+-------+-------+")
    return


#############################################
def enter_move(board,p):
    global x
    global move
    if p == 0:
        x = 0
        move = int(input("Play in number: "))
        if move != 1 and move != 2 and move != 3 and move != 4 and move != 5 and move != 6 and move != 7 and move != 8 and move != 9:
            x = 1
            return x
        for l in range(3):
            for i in range(3):
                if board[l][i] == move:
                    board[l][i] = "O"
                    return board
    else:
        while True:
            move = randrange(10)
            for l in range(3):
                for i in range(3):
                    if board[l][i] == move:
                        board[l][i] = "X"
                        return board


#############################################
def make_list_of_free_fields(board):
    lisT = []
    l = -1
    for lines in board:
        l += 1
        c = 0
        for i in lines:
            c += 1
            if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9:
                lisT.append((l+1,c))     
    return lisT
    

#############################################
def victory_for(board):
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X" or board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X" or board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X" or board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X" or board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X" or board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X" or board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X" or board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        return False
        
    elif board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O" or board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O" or board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O" or board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O" or board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O" or board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O" or board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O" or board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        return True


#############################################
def draw_move(board):
    slots = 0
    for lines in board:
        for i in lines:
            if i == 1 or i == 2 or i == 3 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 9:
                slots = 1
    return slots

    
######################################################################################################################
board = [[7,8,9],[4,"X",6],[1,2,3]]
from random import randrange
global p
h = 0

while True:
    display_board(board) #show the beginner board
    played = enter_move(board,0)

    if played == 1: #incorrect player's move
        print ("Incorrect Option\n")
        continue

    for p in range(2):
        if victory_for(played) == True: #Winner of the game!
            display_board(board)
            print ("Congratulations, YOU WIN!")#
            h = 1
            break
        elif victory_for(played) == False: #Loser ☺
            display_board(board)
            print ("GAME OVER!")#
            h = 1
            break
        elif draw_move(played) == 0: #Draw!!
            print ("DRAW!")
            h = 1
            break

        if p == 0: #CPU time
            enter_move(board,1)
            
    if h == 1:
        break
    print ("\nLines <-> Columns - free to play")
    for lines in make_list_of_free_fields(played):
        e = 0
        for i in range(2):
            if e == 0:
                print (" ",lines[i],end="   <->   ")
                e = 1
                continue
            print (lines[i])

    board = played
