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

def duplicates(lst, item):
  	return [i for i, x in enumerate(lst) if x == item]
def getEmptyPos(lst):
	if(0 in lst and 1 in lst and 2 in lst):
		return -1
	elif(0 in lst and 1 in lst):
		return 2
	elif(0 in lst and 2 in lst):
		return 1
	elif(1 in lst and 2 in lst):
		return 0	
def getValue(x,y,matrix):
	result=0;
	resul=[]
	matrix[x][y]="x"
	if((matrix[0][0] =="-" or matrix[0][0] =="x") and (matrix[0][1] =="-" or matrix[0][1] =="x") and (matrix[0][2] =="-" or matrix[0][2] =="x")):
		result[0]=matrix[0][0]
		result[1]=matrix[0][1]
		result[2]=matrix[0][2]
		if(len(duplicates(result,"x"))==2):
			au=getEmptyPos(len(duplicates(result,"x")))
			if(au==0):
				return [0,0]
			if(au==1):
				return [0,1]
			if(au==2):
				return [0,2]
		result+=1
	if((matrix[1][0] =="-" or matrix[1][0] =="x") and (matrix[1][1] =="-" or matrix[1][1] =="x") and (matrix[1][2] =="-" or matrix[1][2] =="x")):
		result[0]=matrix[1][0]
		result[1]=matrix[1][1]
		result[2]=matrix[1][2]
		if(len(duplicates(result,"x"))==2):
			au=getEmptyPos(len(duplicates(result,"x")))
			if(au==0):
				return [1,0]
			if(au==1):
				return [1,1]
			if(au==2):
				return [1,2]
		result+=1
	if((matrix[2][0] =="-" or matrix[2][0] =="x") and (matrix[2][1] =="-" or matrix[2][1] =="x") and (matrix[2][2] =="-" or matrix[2][2] =="x")):
		result[0]=matrix[2][0]
		result[1]=matrix[2][1]
		result[2]=matrix[2][2]
		if(len(duplicates(result,"x"))==2):
			au=getEmptyPos(len(duplicates(result,"x")))
			if(au==0):
				return [2,0]
			if(au==1):
				return [2,1]
			if(au==2):
				return [2,2]
		result+=1
	if((matrix[0][0] =="-" or matrix[0][0] =="x") and (matrix[1][0] =="-" or matrix[1][0] =="x") and (matrix[2][0] =="-" or matrix[2][0] =="x")):
		result[0]=matrix[0][0]
		result[1]=matrix[1][0]
		result[2]=matrix[2][0]
		if(len(duplicates(result,"x"))==2):
			au=getEmptyPos(len(duplicates(result,"x")))
			if(au==0):
				return [0,0]
			if(au==1):
				return [1,0]
			if(au==2):
				return [2,0]
		result+=1
	if((matrix[0][1] =="-" or matrix[0][1] =="x") and (matrix[1][1] =="-" or matrix[1][1] =="x") and (matrix[2][1] =="-" or matrix[2][1] =="x")):
		result[0]=matrix[0][1]
		result[1]=matrix[1][1]
		result[2]=matrix[2][1]
		if(len(duplicates(result,"x"))==2):
			au=getEmptyPos(len(duplicates(result,"x")))
			if(au==0):
				return [0,1]
			if(au==1):
				return [1,1]
			if(au==2):
				return [2,1]
		result+=1
	if((matrix[0][2] =="-" or matrix[0][2] =="x") and (matrix[1][2] =="-" or matrix[1][2] =="x") and (matrix[2][2] =="-" or matrix[2][2] =="x")):
		result[0]=matrix[0][2]
		result[1]=matrix[1][2]
		result[2]=matrix[2][2]
		if(len(duplicates(result,"x"))==2):
			au=getEmptyPos(len(duplicates(result,"x")))
			if(au==0):
				return [0,2]
			if(au==1):
				return [1,2]
			if(au==2):
				return [2,2]
		result+=1
	if((matrix[0][0] =="-" or matrix[0][0] =="x") and (matrix[1][1] =="-" or matrix[1][1] =="x") and (matrix[2][2] =="-" or matrix[2][2] =="x")):
		result[0]=matrix[0][0]
		result[1]=matrix[1][1]
		result[2]=matrix[2][2]
		if(len(duplicates(result,"x"))==2):
			au=getEmptyPos(len(duplicates(result,"x")))
			if(au==0):
				return [0,0]
			if(au==1):
				return [1,1]
			if(au==2):
				return [2,2]
		result+=1
	if((matrix[2][0] =="-" or matrix[2][0] =="x") and (matrix[1][1] =="-" or matrix[1][1] =="x") and (matrix[0][2] =="-" or matrix[0][2] =="x")):
		result[0]=matrix[2][0]
		result[1]=matrix[1][1]
		result[2]=matrix[0][2]
		if(len(duplicates(result,"x"))==2):
			au=getEmptyPos(len(duplicates(result,"x")))
			if(au==0):
				return [2,0]
			if(au==1):
				return [1,1]
			if(au==2):
				return [0,2]
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
				print(aux1)
				print(aux2)
				if(type(getValue(aux1,aux2,matrix)) is list):
					k=getValue(aux1,aux2,matrix)
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


