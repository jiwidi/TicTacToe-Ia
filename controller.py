from functions import movement
from functions import printMatrix
from functions import getValue
from functions import analyzeMatrix
from functions import isComplete
from functions import getEmptyPos
from functions import getValue
w=3
h=3 
Matrix = [['-' for x in range(w)] for y in range(h)] 
game=1
aux=""
turn=""
print("Welcome to Tic Tac Toe Ia \n")
while(game==1):
    o=1
    resul=["user","computer"]
    while(o==1):
        print("Who start's? the computer or the user?")
        aux=raw_input()
        if(not (aux == "user") and not (aux == "computer")):
            print('Wrong input \n')
    
        else:
            o=2
    if(aux=='user'):
        print('Choose your first movement, first the X coordinate then the Y coordinate \n')
        x=input()
        y=input()
        Matrix=movement(y-1,x-1,"o",Matrix)
        printMatrix(Matrix)
        print('The computer does his movement \n')
        Matrix=movement(1,1,"x",Matrix)
        printMatrix(Matrix)
        turn="o"
    else:
        print('The computer does his movement \n')
        Matrix=movement(1,1,"x",Matrix)
        printMatrix(Matrix)
        turn="o"
    gam=1
    while(gam==1):
        if(isComplete(Matrix)):
            print("Game end, want to restart? tipe yes or no \n")
            u=raw_input()
            if(u=="no"):
                game=0
            gam=0

        elif(turn=="x"):
            print("The computer moves \n")
            aux=analyzeMatrix(Matrix)
            Matrix=movement(aux[0],aux[1],"x",Matrix)
            printMatrix(Matrix)
            turn="o"
        else:
            print("Choose your next movement, first the X coordinate then the Y coordinate \n")
            x=input()
            y=input()
            Matrix=movement(y-1,x-1,"o",Matrix)
            printMatrix(Matrix)
            turn="x"

    
    


