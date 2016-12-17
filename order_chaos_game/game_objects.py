#!/usr/bin/python3.5

# First create a blank board 6x6 
# The tokens in this simple example will take the form of X and O

toks = ['X','O']

board = [['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-']]

# Define the move function

def move(token,horz,vert):
	# check inputs

	while True:
		if token in toks:
			break
		else:
			print('Token must be either X or O')
			token = input('Please choose a token: ')

	while True:		
		if 0<horz<5:
			break
		else:
			print('Horizontal coordinate must be between 0 and 5')
			horz = int(input('Please choose a horizontal coordinate: '))
	
	while True:		
		if 0<vert<5:
			break
		else:
			print('Vertical coordinate must be between 0 and 5')
			vert = int(input('Please choose a vertical coordinate: '))

	# Replace the board coordinate.
	board[vert][horz] = token

	return(board)

# Print board function

def print_board(BOARD):
	print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in board]))

if __name__ == '__main__':
	token1 = input('Token: ')
	hcoord = int(input('Horizontal: '))
	vcoord = int(input('Vertical: '))

	move(token1, hcoord, vcoord)
	print('\nSUCCESS')