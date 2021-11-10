#PLEASE NOTE IN THE SOLUTIONS OUTPUT THAT 1 REPRESENTS A QUEEN, 2 REPRESENTS AND INVALID (UNSAFE) SPACE, AND 0 REPRESENTS A FREE AND SAFE SPACE

import numpy as np

# return first solution
def queen_place_iterative(N):

	#create a blank board of the correct size and shape
	board = np.zeros((N,N))

	solution_valid = False
	permutations = np.array(board)
	permutations = np.reshape(permutations,(1,N,N))

	while(solution_valid == False):
		#pops the last board in the list
		board, permutations = permutations[-1], permutations[:-1]
	
		row = 0
		column  = 0
		queens_placed = 0
		#check the state of the board (to find the last row a queen was placed in)
		while(row != N  and column != N ):

			#count the number of queens
			if(board[row, column] == 1):
			
				queens_placed+=1
				if(queens_placed == N):
					solution_valid = True
					return board
				
			#shift column, if the column was shifted too far, send to next row
			column +=1
			if(column == N ):
				row = row + 1
				column = 0


		#create the next set of boards and append them to the solutions
		row = queens_placed
		for column in range (0,N,1):
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
			



# return array or number of all solutions
def queen_place_iterative_all(N):

	#create a blank board of the correct size and shape
	board = np.zeros((N,N))

	# create two arrays to store board states that are being developed into solutions(permutations)
	# and an array to store solutions
	permutations = np.array(board)
	permutations = np.reshape(permutations,(1,N,N))

	solutions = np.array(board)
	solutions = np.reshape(solutions,(1,N,N))

	# deletes the first board,placed there when the array was created as formating				
	solutions = np.delete(solutions, 0, axis=0)

	
	while(permutations.size != 0):
		#pops the last board in the list
		board = permutations[-1]
		permutations = permutations[:-1]
	
		row = 0
		column  = 0
		queens_placed = 0



		#check the state of the board (to find the last row a queen was placed in)
		while(row != N  and column != N ):
			#count the number of queens
			if(board[row, column] == 1):
				
				queens_placed+=1
				if(queens_placed == N):
					solutions = np.append(solutions,[board], axis=0)
				
			#shift column, if the column was shifted too far, send to next row
			column +=1
			if(column == N ):
				row = row + 1
				column = 0

		if(queens_placed != N):
			#create the next set of boards and append them to the solutions
			row = queens_placed
			for column in range (0,N,1):
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
					
					# print(new_board)
					# add new board to possible solutions 
					permutations = np.append(permutations,[new_board], axis=0)
		

	# return array of all solutions
	return solutions

	# return the number of boards in solutions array
	# return np.size(solutions,0)


# Change this variable to represent the number of queens to solve for
N = 8

###Uncomment call to test each function

print(queen_place_iterative(N))
# print(len(queen_place_iterative_all(N)))

#PLEASE NOTE IN THE SOLUTIONS OUTPUT  THAT 1 REPRESENTS A QUEEN, 2 REPRESENTS AND INVALID (UNSAFE) SPACE, AND 0 REPRESENTS A FREE AND SAFE SPACE
