import pyfiglet
from colorama import Fore, init
import timeit
import random

init(autoreset=True)
X=Fore.RED+"X"
O=Fore.BLUE+"O"

start=timeit.timeit()

def show():
    for row in game_board:
        for cell in row:
            print(cell, end=" ")
        print()

drow = 0
def check_game():
    for i in range(3):
        if game_board[i][0] == X and game_board[i][1] == X and game_board[i][2] == X or game_board[0][i] == X and game_board[1][i] == X and game_board[2][i] == X or game_board[0][2] == X and game_board[1][1] == X and game_board[2][0] == X or game_board[0][0] == X and game_board[1][1] == X and game_board[2][2] == X:
            print("winner:", winner)
            end=timeit.timeit()
            print("time : ", end-start)
            exit()

        if game_board[i][0] == O and game_board[i][1] == O and game_board[i][2] == O or game_board[0][i] == O and game_board[1][i] == O and game_board[2][i] == O or game_board[0][2] == O and game_board[1][1] == O and game_board[2][0] == O or game_board[0][0] == O and game_board[1][1] == O and game_board[2][2] == O:
            print("winner:", winner)
            end=timeit.timeit()
            print("time : ", end-start)
            exit()

        if drow == 9:
            print("Drow!")
            exit()

    

game_board = [["-", "-", "-"],
              ["-", "-", "-"],
              ["-", "-", "-"]]

title = pyfiglet.figlet_format("Tic Tac Toe", font="slant")

print(title)

print("Player vs CPU, enter --> 1\nPlayer vs Player, enter --> 2 \nexit")
print("~~~~~~~~~~~~~~~~~~~")
choise = input("enter choise: ")
show()
print("~~~~~~~~~~~~~~~~~~~")


while True:
    if choise == "exit":
        print("by by")    
        exit()
        
    if choise == "1":
        print("CPU: ")
        while True:
            row = random.randint(0, 2)
            col = random.randint(0, 2)
            if game_board[row][col] == "-":
                game_board[row][col] = X
                break
        drow += 1
        show()
    winner = "CPU"
    check_game()
        

    if choise == "2":
        print("player 1: ")
        while True:
            row = int(input("row: "))
            col = int(input("col: "))

            if 0 <= row <= 2 and 0 <= col <= 2:
                if game_board[row][col] == "-":
                    game_board[row][col] = X
                    break
                else:
                    print("try again")
            print("enter 0-2")
        drow += 1
        show()
    winner = "player 1"
    check_game()

    print("player 2: ")
    while True:
        row = int(input("row: "))
        col = int(input("col: "))

        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "-":
                game_board[row][col] = O
                break
            else:
                print("try again")
        else:
            print("enter 0-2")
    drow += 1     
    show()
    winner = "player 2"
    check_game()

    


