from functions import movement
from functions import printMatrix
w=3
h=3 
Matrix = [['-' for x in range(w)] for y in range(h)] 
game=1
aux=""
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
        print('Choose your first movement, first the X coordinate then the Y coordinate')
        x=input()
        y=input()
        Matrix=movement(x,y,"o",Matrix)
        print(Matrix)
    else:
    	print('The computer does his movement')
    	Matrix=movement(1,1,"x",Matrix)
    	print(Matrix)

