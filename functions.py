def movement( x,y,player,matrix ):
    if(isinstance( x, int ) and isinstance( y, int )and x<3 and x>=0 and y<3 and y>=0):
        if(matrix[x][y]=='-'):
            matrix[x][y]=player 
        else:
            print("You can't place your token there, there is already one ")   

    

    return matrix
def printMatrix(matrix):
    print(matrix[0]+"\n")
    print(matrix[1]+"\n")
    print(matrix[2]+"\n")

