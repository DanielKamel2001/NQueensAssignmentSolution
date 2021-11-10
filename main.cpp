#include <iostream>
#include <vector>
#include <array>


const int N = 8;

//counts the amount of queens placed in an board
//(an array each value represents the column in each row, where -1 represents rows that are empty)
int num_of_queens_placed(std::array<int, N> board) {
 	int queens_placed = 0;
	
	for (int row = 0; row < N; row++) {
		if ( board[row]  >= 0 && board[row] <= N) {
			queens_placed++;
		}
	}

	return queens_placed;
}

//returns an array representing the first solution where the order of elements represntes row and value represents column of a queen
std::array<int, N> queen_place_1() {
	std::vector<std::array<int, N>> permutations;
	std::vector<std::array<int, N>> solutions;
	permutations.push_back({});
	permutations.back().fill(-1);
	std::array<int, N> store;
	
	while (permutations.size() != 0) {
		
		//check board
		int queens_placed;
		queens_placed = num_of_queens_placed(permutations.back());  


		// if board is full return it as a solution
		if (queens_placed == N) {
			//return permutations.back();
			solutions.push_back(permutations.back());
			permutations.pop_back();

		}else{
			//
			//place a queen
			//
			
			//storing last array in permutations in a temp space
			for (int i = 0; i < N; i++){
				store[i] = permutations.back()[i];
			}

			//removing it from permutations
			permutations.pop_back();
			
			//create an array of nums that represent possible spaces for a queen to be placed in the next row (1 -> N)
			std::vector<int> possible;
			int x; //used to calculate if the 
			bool valid_space;

			//if not the first queen to be placed, else every number is valid
			if (queens_placed >= 1) {
				//for every number 0 -> N
				for (int i = 0; i < N; i++) {
					
					valid_space = true;
					
					//for every row that already has a queen in it
					for (int row = 0; row < queens_placed; row++) {
						x = queens_placed - row;
						
						//if the that queen blocks that space in the row x then set it so that it will not be added to possibles
						if ((-1 * x + store[row]) == i || (store[row]) == i || (1 * x + store[row]) == i) {
							valid_space = false; 
						}
					}

					if(valid_space == true){ possible.push_back(i); }
				}
			}else{
				for (int i = 0; i < N; i++) {
					possible.push_back(i);
				}
			}
			


			if (possible.size() != 0) {
				for (int number : possible) {
					std::array<int, N> write;
					write = store;
					write[queens_placed] = number;
					permutations.push_back(write);
				}
			}

		}
	}
	////printing all solutions
	/*for (int i = 0; i < solutions.size(); i++) {
		for (int j = 0; j < N; j++) {
			std::cout << solutions[i][j];
		}
		std::cout << std::endl;
	}*/

	std::cout << "Number of solutions found: " << solutions.size() << std::endl;
	return solutions[1];
}

int main() {
	
	std::array<int, N> board = queen_place_1();
	std::cout << "first soluton found:";
	for (int j = 0; j < N; j++) {
		std::cout <<" "<< board[j];
	}
	std::cout << std::endl; 

	return 1;
}