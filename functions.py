def movement( x,y,player,matrix ):
    if(isinstance( x, int ) and isinstance( y, int )and x<3 and x>=0 and y<3 and y>=0):
        if(matrix[x][y]=='-'):
            matrix[x][y]=player 
        else:
            print("You can't place your token there, there is already one ")   

    

    return matrix
def printMatrix(matrix):
    print(matrix[0])
    print(matrix[1])
    print(matrix[2])

def getValue(x,y,matrix):
	result=0
	goal=["x","x","x"]
	resul=[]
	matrix[x][y]="x"
	if((matrix[0][0] =="-" or matrix[0][0] =="x") and (matrix[0][1] =="-" or matrix[0][1] =="x") and (matrix[0][2] =="-" or matrix[0][2] =="x")):
		resul.append(matrix[0][0])
		resul.append(matrix[0][1])
		resul.append(matrix[0][2])
		
		if(resul==goal):
			matrix[x][y]="-"
			return[x,y]
		
		resul=[]	
		result+=1
	if((matrix[1][0] =="-" or matrix[1][0] =="x") and (matrix[1][1] =="-" or matrix[1][1] =="x") and (matrix[1][2] =="-" or matrix[1][2] =="x")):
		resul.append(matrix[1][0])
		resul.append(matrix[1][1])
		resul.append(matrix[1][2])
		
		if(resul==goal):
			matrix[x][y]="-"
			return[x,y]
			
		resul=[]
		result+=1
	if((matrix[2][0] =="-" or matrix[2][0] =="x") and (matrix[2][1] =="-" or matrix[2][1] =="x") and (matrix[2][2] =="-" or matrix[2][2] =="x")):
		resul.append(matrix[2][0])
		resul.append(matrix[2][1])
		resul.append(matrix[2][2])
		if(resul==goal):
			matrix[x][y]="-"
			return[x,y]
		
		resul=[]	
		result+=1
	if((matrix[0][0] =="-" or matrix[0][0] =="x") and (matrix[1][0] =="-" or matrix[1][0] =="x") and (matrix[2][0] =="-" or matrix[2][0] =="x")):
		resul.append(matrix[0][0])
		resul.append(matrix[1][0])
		resul.append(matrix[2][0])
		if(resul==goal):
			matrix[x][y]="-"
			return[x,y]
		
		resul=[]	
		result+=1
	if((matrix[0][1] =="-" or matrix[0][1] =="x") and (matrix[1][1] =="-" or matrix[1][1] =="x") and (matrix[2][1] =="-" or matrix[2][1] =="x")):
		resul.append(matrix[0][1])
		resul.append(matrix[1][1])
		resul.append(matrix[2][1])
		if(resul==goal):
			matrix[x][y]="-"
			return[x,y]
		
		resul=[]	
		result+=1
	if((matrix[0][2] =="-" or matrix[0][2] =="x") and (matrix[1][2] =="-" or matrix[1][2] =="x") and (matrix[2][2] =="-" or matrix[2][2] =="x")):
		resul.append(matrix[0][2])
		resul.append(matrix[1][2])
		resul.append(matrix[2][2])
		if(resul==goal):
			matrix[x][y]="-"
			return[x,y]
		
		resul=[]	
		result+=1
	if((matrix[0][0] =="-" or matrix[0][0] =="x") and (matrix[1][1] =="-" or matrix[1][1] =="x") and (matrix[2][2] =="-" or matrix[2][2] =="x")):
		resul.append(matrix[0][0])
		resul.append(matrix[1][1])
		resul.append(matrix[2][2])
		if(resul==goal):
			matrix[x][y]="-"
			return[x,y]
		
		resul=[]	
		result+=1
	if((matrix[2][0] =="-" or matrix[2][0] =="x") and (matrix[1][1] =="-" or matrix[1][1] =="x") and (matrix[0][2] =="-" or matrix[0][2] =="x")):
		resul.append(matrix[2][0])
		resul.append(matrix[1][1])
		resul.append(matrix[0][2])
		if(resul==goal):
			matrix[x][y]="-"
			return[x,y]
		
		resul=[]
		result+=1
	matrix[x][y]="-"	

	return result
def analyzeMatrix(matrix):
	max=0
	dx=-1
	dy=-1
	aux1=-1
	aux2=-1
	for val in matrix:
		aux1+=1
		for va in val:
			aux2+=1
			if(va=="-"):
				if(type(getValue(aux1,aux2,matrix)) is list):
					print("sol")
					k=getValue(aux1,aux2,matrix)
					end=True
					return [k[0],k[1]]
				elif(getValue(aux1,aux2,matrix)>max):
					max=getValue(aux1,aux2,matrix)
					dx=aux1
					dy=aux2
		aux2=-1
	return [dx,dy]

def isComplete(matrix):
	for val in matrix:
		for va in val:
			if(va=="-"):
			    return False

	return True


