from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from random import randrange
import logging

log = logging.getLogger(__name__)

from game.models import Board, Tile

# Create new Game and Render
def index(request):
	board_id, tiles = newBoard()
	board = get_object_or_404(Board, pk=board_id)
	return render(request, 'game/detail.html', {'board': board, 'tiles': tiles})

# Current Game Render
def detail(request, board_id):
	if request.method == 'POST':
		x = request.POST['x']
		y = request.POST['y']
		shift = request.POST['shift']
		if shift == 'off':
			reveal(board_id, x, y)
		if shift == 'on':
			mark(board_id, x, y)

	board = get_object_or_404(Board, pk=board_id)
	tiles = Tile.objects.filter(board=board) # Cache tiles to not have to do this everytime
	return render(request, 'game/detail.html', {'board': board, 'tiles': tiles})


### Function Code

# Mark tile
def mark(board_id, x, y):
	tile = Tile.objects.filter(board=board_id,
	 x=x, y=y)
	tile.update(marked = True)

# Reveal tiles
def reveal(board_id, x, y):
	try:
		tile = Tile.objects.filter(board=board_id,
		 x=x, y=y)
		if tile[0].revealed == False:
			tile.update(revealed = True)
			x = int(x)
			y = int(y)
			if tile[0].mine == False and tile[0].value == 0:
				if x != 0:
					reveal(board_id, x-1, y)
				if x != 9:
					reveal(board_id, x+1, y)
				if y != 0:
					reveal(board_id, x, y-1)
				if y != 9:
					reveal(board_id, x, y+1)
	except Exception as inst:
		print inst
		
	

# Make new Board
def newBoard():
	newboard = Board.objects.create(width=10, 
		height=10, numberOfMines=25)
	board_id = newboard.id
	board = get_object_or_404(Board, pk=board_id)
	tiles = []
	# Create tiles
	for y in range(0, newboard.width):
		for x in range(0, newboard.height):
			# 30% will be mines
			if randrange(9) < 1:
				tiles.append(Tile.objects.create(board=board, mine=True, revealed=False, marked=False, value=0, x=x, y=y))
			# 70% will be empty
			else:
				tiles.append(Tile.objects.create(board=board, mine=False, revealed=False, marked=False, value=0, x=x, y=y))
	# Update tile value if adjacent to mine
	for tile in tiles:
		position = (tile.y*10) + tile.x
		# Check left right
		if tile.x != 0:
			if tiles[position - 1].mine == True:
				tile.value += 1
		if tile.x != 9:
			if tiles[position + 1].mine == True:
				tile.value += 1
		# Check top left, center, right
		if tile.y != 0:
			if tiles[position - 10].mine == True:
				tile.value += 1
			if tile.x != 9:
				if tiles[position - 9].mine == True:
					tile.value += 1
			if tile.x != 0:
				if tiles[position - 11].mine == True:
					tile.value += 1
		# Check bottom left, center, right
		if tile.y != 9:
			if tiles[position + 10].mine == True:
				tile.value += 1
			if tile.x != 0:
				if tiles[position + 9].mine == True:
					tile.value += 1
			if tile.x != 9:
				if tiles[position + 11].mine == True:
					tile.value += 1

		t = Tile.objects.filter(board=board_id,
		 		x=tile.x, y=tile.y)
		t.update(value = tile.value)
	return (board_id, tiles)