#!/usr/bin/python3.5

# This script executes game until winner is found or all squares are filled

import game_objects as game
from itertools import cycle

opening_text = open('opening_text.txt')
opening_text = opening_text.read()

print(opening_text)

# create tokens and board

toks = ['X','O']
board = [['.' for col in range(6)] for row in range(6)]

# Commence alternating for loop between players. Break when all squares are filled or player wins

for player in cycle(['Player:1', 'Player:2']):
	print(player+"'s turn\n")
	token = input(player + ' please choose a token: ').upper()
	row = int(input('Please choose a row: '))
	col = int(input('Please choose a column: '))

	board = game.move(token, row, col, board)
	if game.check_board(board, 'X') == True:
		print(player+' WINS!')
		break
	elif game.check_board(board, 'O') == True:
		print(player+' WINS!')
		break
	else:
		pass

	game.print_board(board)



