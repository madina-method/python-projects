import random
import time
board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def show():
    print(board[0], "|", board[1], "|", board[2])
    print(board[3], "|", board[4], "|", board[5])
    print(board[6], "|", board[7], "|", board[8])

def isFree(pos):
    if board[pos] != "X" and board[pos] != "O":
        return True
    else:
        return False

def compAI():
    n = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(n)
    for i in range(9):
        if isFree(n[i]):
            if isWin(n[i]):
                return n[i]
            if board[]
                return index
        if board[4] != :
            
            board[n[i]] = comp
            break
def isWin(letter):
    if (board[0]==board[1]==board[2]==letter or board[3]==board[4]==board[5]==letter or
        board[6]==board[7]==board[8]==letter or board[0]==board[3]==board[6]==letter or
        board[1]==board[4]==board[7]==letter or board[2]==board[5]==board[8]==letter or
        board[0]==board[4]==board[8]==letter or board[2]==board[4]==board[6]==letter):
        return True

counter = 0
    
me = input("Choose the side X | O\n").upper()
if me == "X":
    comp = "O"
else:
    comp = "X"

show()

while True:

    while True:
        pos = int(input("Choose the position\n"))
        if isFree(pos):
            board[pos] = me
            break

    show()
    if isWin(me):
        print("You won!")
        break
    counter+=1
    if counter == 9:
        print("Draw!")
        break

    
    index = compAI()
    board[index] = comp
    print("\nComputer is thinking . . .")
    time.sleep(3)
    show()

    if isWin(comp):
        print("Computer won!")
        break
    counter+=1
    if counter == 9:
        print("Draw!")
        break
