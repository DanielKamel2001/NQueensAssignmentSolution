import numpy as np

# return first solution
def queen_place_iterative(N):

	#create an array where index represents row and value reps. coloumn
	board = np.full(N,-1)
	# print(board)

	solution_valid = False
	permutations = np.array(board)
	permutations = np.reshape(permutations,(1,N))

	solutions = np.array(board)
	solutions = np.reshape(solutions,(1,N))
	solutions = np.delete(solutions, 0, axis=0)
	

	while(len(permutations) != 0):# while(solution_valid == False):

		#pops the last board in the list
		# print(permutations)
		board, permutations = permutations[-1], permutations[:-1]


		queens_placed = 0
		#check the state of the board (to find the last row a queen was placed in)
		for row in range(0,len(board)):
			if (board[row] != -1):
				queens_placed += 1 
				if (queens_placed == N):
					solution_valid = True
					solutions = np.append(solutions,[board], axis=0) 
					# print(board)
					

		#create the next set of boards and append them to the solutions
		possible = np.arange(N)

		
		if queens_placed != 0:
			for i in range(0,queens_placed,1):
				x = queens_placed - i
				possible = possible[possible != (-1*x) +board[i]]
				possible = possible[possible != board[i]]
				possible = possible[possible != (x) +board[i]]
			

		if len(possible) != 0:
			for number in possible:
				new_board = np.copy(board)
				new_board[queens_placed] = number
				permutations = np.append(permutations,[new_board], axis=0) 
				
	return solutions

N = 8

###Uncomment call to test each function

print(len(queen_place_iterative(N)))