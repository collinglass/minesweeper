from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from game.models import Board, Tile

def index(request):
	newboard = Board.objects.create(width=10, 
		height=10, numberOfMines=25)
	board = get_object_or_404(Board, pk=newboard.id)
	tiles = []
	for y in range(0, newboard.width):
		for x in range(0, newboard.height):
			if x % 2 == 0 and y % 2 == 0:
				tiles.append(Tile.objects.create(board=board, mine=True, revealed=False, marked=False, value=0, x=x, y=y))
			else:
				tiles.append(Tile.objects.create(board=board, mine=False, revealed=False, marked=False, value=0, x=x, y=y))
	for tile in tiles:
		position = (tile.y*10) + tile.x
		if tile.y != 0:
			if tiles[position - 10].mine == True:
				tile.value += 1
			if tile.x != 9:
				if tiles[position - 9].mine == True:
					tile.value += 1
			if tile.x != 0:
				if tiles[position - 11].mine == True:
					tile.value += 1
		if tile.y != 9:
			if tiles[position + 10].mine == True:
				tile.value += 1
			if tile.x != 0:
				if tiles[position + 9].mine == True:
					tile.value += 1
			if tile.x != 9:
				if tiles[position + 11].mine == True:
					tile.value += 1

	return render(request, 'game/detail.html', {'board': board, 'tiles': tiles})

def detail(request, board_id):
	if request.method == 'POST':
		tile = Tile.objects.filter(board=board_id,
		 x=request.POST['x'], y=request.POST['y'])
		tile.update(revealed = True)
		print (tile[0].revealed)
	board = get_object_or_404(Board, pk=board_id)
	tiles = Tile.objects.filter(board=board) # Cache tiles to not have to do this everytime
	return render(request, 'game/detail.html', {'board': board, 'tiles': tiles})

def results(request, board_id):
	return HttpResponse("You're looking at the results of board %s." % board_id)

def turn(request, board_id):
	return HttpResponse("You're turn on board %s." % board_id)

# Create your views here.
