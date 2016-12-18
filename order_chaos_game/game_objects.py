#!/usr/bin/python3.5

# Contains the functions required to create the game
# These functions include move, which allows one to move a piece on the board

# The tokens in this simple example will take the form of X and O

# ---- Preliminary function definition ----- #

# Print board function

def print_board(BOARD):
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in BOARD]))


# pos_check 1 check the move is correct token and on the board

def pos_check_1(TOKEN, ROW, COL, BOARD):
	# check position is on on board and valid token

	while True:
		if TOKEN in toks:
			break
		else:
			print('Token must be either X or O')
			TOKEN = input('Please choose a token: ')

	while True:		
		if 0<=ROW<=5:
			break
		else:
			print('Row must be between 0 and 5')
			ROW = int(input('Please choose another row: '))
	
	while True:		
		if 0<=COL<=5:
			break
		else:
			print('Column must be between 0 and 5')
			COL = int(input('Please choose a column: '))

	return(TOKEN, ROW, COL)

# pos_check 2 checks there is no overlap with another piece

def pos_check_2(ROW, COL, BOARD):
	# Check position is not overlapping other piece

	while True:
		if BOARD[ROW][COL] in toks:
			print('\n INVALID MOVE! {} already located at [{},{}] \n'.format(BOARD[ROW][COL], ROW, COL))
			print_board(BOARD)
			print('\n')
			ROW = int(input('Please choose another row: '))
			COL = int(input('Please choose another column: '))
		else:
			break

	return(ROW, COL)

# Define the move function

def move(TOKEN, ROW, COL, BOARD):

	# Check positions
	TOKEN, ROW, COL = pos_check_1(TOKEN, ROW, COL, BOARD)
	ROW, COL = pos_check_2(ROW, COL, BOARD)
	BOARD[ROW][COL] = TOKEN
	return(BOARD)

# Define column function. Will be used in win function

def column(BOARD, i):
	return([row[i] for row in BOARD])

# Define win function. Check tokens individually.

def win_check(BOARD, TOKEN):
	# Check rows first

	for row in range(6):
		# Check if value in row
		try:							
			tokloc = BOARD[row].index(TOKEN)
			if tokloc<=2:
				if all(ind == TOKEN for ind in BOARD[row][tokloc:tokloc+5]):
					print('YOU WON!')
					print_board(BOARD)
					del(tokloc)		# del tokloc variable
					break

		except ValueError:
			pass

	# Check columns
	for col in range(6):
		board_col = column(BOARD,col)

		# Check if value in row
		try:							
			tokloc = board_col.index(TOKEN)
			if tokloc<=2:
				if all(ind == TOKEN for ind in board_col[tokloc:tokloc+5]):
					print('YOU WON!')
					print_board(BOARD)
					del(tokloc)
					break

		except ValueError:
			pass

if __name__ == '__main__':
	# Define prelims

	toks = ['X','O']

	board = [['-' for col in range(6)] for row in range(6)]


	# token1 = input('Token: ')
	# hcoord = int(input('Horizontal: '))
	# vcoord = int(input('Vertical: '))

	# # move(token1, hcoord, vcoord)
	# print('\nSUCCESS')