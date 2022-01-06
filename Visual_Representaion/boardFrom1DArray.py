import pygame
import numpy as np
import time
import os

from pygame.constants import K_RETURN




# Draws on the display the representation of the board
def make_board(board):
    #reset the display to be a black screen
    pygame.draw.rect(display,black,(0,0,display_size,display_size))

    offset = False # controls the checkered pattern

    # for every row draw a white square in every other column
    # offset if the row is odd
    for row in range (0,N,1):
        for column in range (0,N,2):
            if(offset):
                pygame.draw.rect(display, white, (square_size+(column*square_size),row*square_size,square_size,square_size))
            else:
                pygame.draw.rect(display, white, (column*square_size,row*square_size,square_size,square_size))
        offset = not offset

    for x in range (0,len(board),1):
        display.blit(queen_image,(board[x]*square_size,x*square_size))
    pygame.display.update()

def wait():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                os.sys.exit()
            if event.type ==pygame.KEYDOWN and (event.key == K_RETURN):
                return

# returns a list of solutions
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
        
        # display the last board
        make_board(board)
        time.sleep(0.15)

        #check the state of the board (to find the last row a queen was placed in)
        queens_placed = 0
        for row in range(0,len(board)):
            if (board[row] != -1):
                queens_placed += 1 
                if (queens_placed == N):
                    
                    # add board to solutions array
                    solutions = np.append(solutions,[board], axis=0) 

                    # print the array format of the board
                    print("solution found:{}".format(board))

                    # display message on display of the board being found
                    textStyle = pygame.font.Font('freesansbold.ttf',12)
                    textSurface = textStyle.render("Solution Found! Press enter to continue search ", True, red)
                    TextRect =  textSurface.get_rect()
                    TextRect.topleft = (0,0)
                    display.blit(textSurface, TextRect)
                    pygame.display.update()

                    # wait till the user hits enter to continue the 
                    wait()
                  

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
                # 
                permutations = np.append(permutations,[new_board], axis=0) 
    return solutions

N = 8

# colour objects
black = (0,0,0)
white = (255,255,255)
red= (255,0,0)

pygame.init()

#the display
display_size = 600
display = pygame.display.set_mode((display_size,display_size))
pygame.display.set_caption("Daniel's N-Queens Solution")

square_size = display_size/N #sets the size of the chess spaces

#image to represent a queen piece and resizing to fit 
queen_image = pygame.image.load('queen.png')
queen_image = pygame.transform.scale(queen_image,(display_size/N,display_size/N)) 

queen_place_iterative(N)

