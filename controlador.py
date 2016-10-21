
w=3
h=3 
Matrix = [[0 for x in range(w)] for y in range(h)] 

print("Welcome to Tic Tac Toe Ia \n")

o=1
resul=["user","computer"]
while(o==1):
	print("Who start's? the computer or the user?")
	aux=raw_input()
	print(aux)
	if(not (aux == "user") and not (aux == "computer")):
		print('Wrong input')
	
	else:
		o=2
print(Matrix)