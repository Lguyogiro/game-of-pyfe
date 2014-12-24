import random
import sys

class Life(object):

	def __init__(self, height, width):
		self.height = height
		self.width = width
		self.alive_symbol = '@'
		self.dead_symbol = '_'
		self.board_display = []
		self.board_coords = {}

	def __str__(self):
		display = ''
		for row in self.board_display:
			display += " ".join([str(el) for el in row]) + "\n"
		return display

	def board_init(self):
		new_board_coords = {}
		options = [self.alive_symbol, self.dead_symbol]
		for row in range(0, self.width):
			for col in range(0, self.height):
				new_board_coords[(col+1, row+1)] = random.choice(options)
		self.board_coords = new_board_coords
		self.render_board()

	def render_board(self):
		self.board_display = [[self.board_coords[(col + 1, row + 1)] for 
							  col in range(0, self.height)] for 
							  row in range(0,self.width)]

	def neighbors(self, cell):
		return [(cell[0], cell[1] - 1), 
				(cell[0], cell[1] + 1),
				(cell[0] - 1, cell[1]), 
				(cell[0] + 1, cell[1]),
				(cell[0] + 1, cell[1] - 1), 
				(cell[0] - 1, cell[1] + 1),
				(cell[0] - 1, cell[1] - 1), 
				(cell[0] + 1, cell[1] + 1)]

	def eval_cell(self, cell, board):
		live_neighbors = len([n for n in self.neighbors(cell) if 
						     (n[0] > 0 and n[1] > 0) and 
						     (n[0] <= self.height and n[1] <= self.width) 
						     and board[n] == self.alive_symbol])
		return (1 < live_neighbors < 4 
				if board[cell] == self.alive_symbol else live_neighbors == 3)

	def cycle(self):
		new_board = {}
		for cell in self.board_coords:
			if self.board_coords[cell] == self.alive_symbol:
				if self.eval_cell(cell, self.board_coords):
					new_board[cell] = self.alive_symbol
				else:
					new_board[cell] = self.dead_symbol
			else:
				if self.eval_cell(cell, self.board_coords):
					new_board[cell] = self.alive_symbol
				else:
					new_board[cell] = self.dead_symbol
		self.board_coords = new_board
		self.render_board()


if __name__ == '__main__':
	if len(sys.argv) == 3:
		height, width = int(sys.argv[1]), int(sys.argv[2])
	else:
		height, width = 20, 20
	game = Life(height, width)
	game.board_init()
	print game
	action = raw_input("")
	while action.lower() != 'q':
		game.cycle()
		print game
		action = raw_input("")
