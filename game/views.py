from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from random import randrange

from game.models import Board, Tile

def index(request):
	board_id, tiles = newBoard()
	board = get_object_or_404(Board, pk=board_id)

	return render(request, 'game/detail.html', {'board': board, 'tiles': tiles})

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

def results(request, board_id):
	return HttpResponse("You're looking at the results of board %s." % board_id)

def turn(request, board_id):
	return HttpResponse("You're turn on board %s." % board_id)


# Mark tile
def mark(board_id, x, y):
	tile = Tile.objects.filter(board=board_id,
	 x=x, y=y)
	tile.update(marked = True)

# Reveal tile
def reveal(board_id, x, y):
	if tile[0].revealed == False:
		tile = Tile.objects.filter(board=board_id,
		 x=x, y=y)
		tile.update(revealed = True)
		#if tile[0].mine == False and tile[0].value == 0:
		#	if not x == 0:
		#		tempx = x-1
		#		print (tempx)
		#		reveal(board_id, tempx, y)
		#	if not x == 9:
		#		tempx = x+1
		#		reveal(board_id, tempx, y)
		#	if not y == 0:
		#		tempy = y-1
		#		reveal(board_id, x, tempy)
		#	if not y == 9:
		#		tempy = y+1
		#		reveal(board_id, x, tempy)
		
	

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