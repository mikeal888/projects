#!/usr/bin/python3.5

# Contains the functions required to create the game
# These functions include move, which allows one to move a piece on the board

# The tokens in this simple example will take the form of X and O

# ---- Preliminary function definition ----- #

# pos_check 1 and 2 check the move is correct token and on the board, and that move does not overlap with other piece

def pos_check_1(TOKEN, ROW, COL, BOARD):
	# check position is on on board and valid token

	while True:
		if TOKEN in toks:
			break
		else:
			print('Token must be either X or O')
			TOKEN = input('Please choose a token: ')

	while True:		
		if 0<ROW<5:
			break
		else:
			print('Row must be between 0 and 5')
			ROW = int(input('Please choose another row: '))
	
	while True:		
		if 0<COL<5:
			break
		else:
			print('Column must be between 0 and 5')
			COL = int(input('Please choose a column: '))

def pos_check_2(TOKEN, ROW, COL, BOARD):
	# Check position is not overlapping other piece

	while True:
	if BOARD[ROW][COL] in toks:
		print('Invalid move! {} already located at [{},{}]'.format(BOARD[ROW][COL], ROW, COL))
		print('Please choose another coordinate')
	else:
		break

def move(TOKEN, ROW, COL, BOARD):




# Print board function

def print_board(BOARD):
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in BOARD]))

# Define column function. Will be used in win function

def column(BOARD, i):
	return([row[i] for row in BOARD])

# Define win function

def win_check(BOARD):
 	# Need to check rows and columns for 5 'O' or 'X' in a row
 	# Check rows first

 	for i in



if __name__ == '__main__':
	# Define prelims

	toks = ['X','O']

	board = [['-' for col in range(6)] for row in range(6)]

	token1 = input('Token: ')
	hcoord = int(input('Horizontal: '))
	vcoord = int(input('Vertical: '))

	move(token1, hcoord, vcoord)
	print('\nSUCCESS')