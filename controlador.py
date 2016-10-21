from functions import movement
from functions import printMatrix
from functions import getValue
from functions import analyzeMatrix
from functions import isComplete
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
            print('Wrong input')
    
        else:
            o=2
    if(aux=='user'):
        print('Choose your first movement, first the Y coordinate then the X coordinate')
        x=input()
        y=input()
        Matrix=movement(x,y,"o",Matrix)
        printMatrix(Matrix)
        turn="x"
    else:
        print('The computer does his movement')
        Matrix=movement(1,1,"x",Matrix)
        printMatrix(Matrix)
        turn="o"
    gam=1
    while(gam==1):
        if(isComplete(Matrix)):
            print("Game end, want to restart? tipe yes or no")
            u=input()
            if(u=="no"):
                game=0
            gam=0

        elif(turn=="x"):
            print("The computer moves")
            aux=analyzeMatrix(Matrix)
            
            Matrix=movement(aux[0],aux[1],"x",Matrix)
            printMatrix(Matrix)
            turn="o"
        else:
            print("Choose your next movement, first the y coordinate then the x coordinate")
            x=input()
            y=input()
            Matrix=movement(x,y,"o",Matrix)
            printMatrix(Matrix)
            turn="x"

    
    


