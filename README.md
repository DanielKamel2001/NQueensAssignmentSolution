# NQueensAssignmentSolution
An assignment from my Data Structures course. 

N-Queens is a known algorithms problem of how to configure N amount of queens on a chess board of N by N size such that no queen can threaten another queen on the board (i.e. capture another queen in 1 move.)

The inital assignment required both an iterative and recursive solution which were written in python and included here. 

I later took it upon myself to improve the space complexity of the algorithm by changing the format the board states were stored in. They were orignally stored as N by N arrays where each spaces on the game boared were indexed by real chess coordinate systems. This system was revised to a 1D array representation using the assumption that a board will never have more than 1 queen in any row.

Later the 1D array version was converted to C++

Visual representations of boards are here: run the file in the Visual Representations folder with the queen.png file in the same directory
Program displays each step of finding the solution and pauses when a soltion is found