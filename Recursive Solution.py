#PLEASE NOTE IN THE SOLUTIONS OUTPUT THAT 1 REPRESENTS A QUEEN, 2 REPRESENTS AND INVALID (UNSAFE) SPACE, AND 0 REPRESENTS A FREE AND SAFE SPACE

import numpy as np
 
times= 0
#return the first solution
def queen_place_recursive(board, N ):

	# is the board valid/ full
	row = 0
	column  = 0
	queens_placed = 0
	solution_valid = False


	#check the state of the board
	while(row != N  and column != N ):

		#count the number of queens
		if(board[row, column] == 1):
			
			queens_placed+=1
			if(queens_placed == N):
				solution_valid = True
	
				
		#shift column, if the column was shifted too far, send to next row
		column +=1
		if(column == N ):
			row = row + 1
			column = 0

	if(solution_valid):
		return board
	else:
		#create an array of N boards, each having 1 queen placed in every possible slot of the relevant row, 
		permutations = np.array(board)
		permutations = np.reshape(permutations,(1,N,N))

		row = (queens_placed)
		column  = 0
		while(column != N ):
			
			#if the space is free place a queen on a copy board
			if (board[row, column] == 0):
				new_board = np.copy(board) 
					
				new_board[row,column] = 1
			
				#invalidate the row and column that the queen was placed in
				for i in range(0, N ,1):
					if (new_board[row, i] == 0):
						new_board[row, i] = 2
					if (new_board[i, column] == 0):
						new_board[i, column] = 2

				#invalidate the diagonals of the queen
				#bottom right
				k = 0
				while(row + k < N  and column + k < N ):
					if (new_board[row + k, column + k] == 0):
						new_board[row + k, column + k] = 2
					k+=1
		
				#top left
				k = 0
				while(row - k >= 0  and column - k >=0 ):
					if (new_board[row - k, column - k] == 0):
						new_board[row - k, column - k] = 2
					k+=1

				#bottom left
				k = 0 
				while(row + k < N  and column - k >= 0):
					if (new_board[row + k, column - k] == 0):
						new_board[row + k, column - k] = 2
					k+=1
				
				#top right
				k = 0 
				while(row - k >= 0 and column + k < N):
					if (new_board[row - k, column + k] == 0):
						new_board[row - k, column + k] = 2
					k+=1

				# add new board to possible solutions 
				permutations = np.append(permutations,[new_board], axis=0)
						
			#shift column, ###if the column was shifted too far, send to next row
			column +=1
			

		#delete the first(a blank, used to format)
		permutations = np.delete(permutations, 0, axis=0)
				
		for i in range(0,len(permutations),1):
			answer = queen_place_recursive(permutations[i], N)
			if (answer is not None):
				return answer

#print all solutions 
def queen_place_recursive_all(board, N ):
	# is the board valid/ full
	row = 0
	column  = 0
	queens_placed = 0
	solution_valid = False


	#check the state of the board
	while(row != N  and column != N ):

		#count the number of queens
		if(board[row, column] == 1):
			
			queens_placed+=1
			if(queens_placed == N):
				solution_valid = True
	
				
		#shift column, if the column was shifted too far, send to next row
		column +=1
		if(column == N ):
			row = row + 1
			column = 0



	if(solution_valid):
		print(board,'\n')
		global times
		times += 1
	else:
		#create an array of boards, each having 1 queen placed in every possible slot
		permutations = np.array(board)
		permutations = np.reshape(permutations,(1,N,N))

		row = (queens_placed)
		column  = 0
		queens_placed = 0
		while(column != N ):
			
			#if the space is free place a queen on a copy board
			if (board[row, column] == 0):
				new_board = np.copy(board) 
					
				new_board[row,column] = 1
			
				#invalidate the row and column that the queen was placed in
				for i in range(0, N ,1):
					if (new_board[row, i] == 0):
						new_board[row, i] = 2
					if (new_board[i, column] == 0):
						new_board[i, column] = 2

				#invalidate the diagonals of the queen
				#bottom right
				k = 0
				while(row + k < N  and column + k < N ):
					if (new_board[row + k, column + k] == 0):
						new_board[row + k, column + k] = 2
					k+=1
		
				#top left
				k = 0
				while(row - k >= 0  and column - k >=0 ):
					if (new_board[row - k, column - k] == 0):
						new_board[row - k, column - k] = 2
					k+=1





				#bottom left
				k = 0 
				while(row + k < N  and column - k >= 0):
					if (new_board[row + k, column - k] == 0):
						new_board[row + k, column - k] = 2
					k+=1
				
				#top right
				k = 0 
				while(row - k >= 0 and column + k < N):
					if (new_board[row - k, column + k] == 0):
						new_board[row - k, column + k] = 2
					k+=1

				# add new board to possible solutions 
				permutations = np.append(permutations,[new_board], axis=0)
						
			#shift column, if the column was shifted too far, send to next row
			column +=1
			

		#delete the first(a blank, used to format)
		permutations = np.delete(permutations, 0, axis=0)
				
		for i in range(0,len(permutations),1):
			answer = queen_place_recursive_all(permutations[i], N)

# Change this variable to represent the number of queens to solve for
N = 9

#creating the board N by N
board = np.zeros((N,N))

###Uncomment call to test each function

# print(queen_place_recursive(board,N))
# queen_place_recursive_all(board,N) # does not need a print statement, print statement in function prints boards as found, global variable was used to test number of solutions produced
# print(times)
#PLEASE NOTE IN THE SOLUTIONS OUTPUT THAT 1 REPRESENTS A QUEEN, 2 REPRESENTS AND INVALID (UNSAFE) SPACE, AND 0 REPRESENTS A FREE AND SAFE SPACE
