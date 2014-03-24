from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

import logging

log = logging.getLogger(__name__)

from game.models import Board, Tile

# Create new Game and Render
def index(request):
	# New board
	board = Board.objects.create(width=10, height=10)
	# Create new board and tiles
	tiles = board.newBoard()
	# Render details page
	return render(request, 'game/detail.html', {'board': board, 'tiles': tiles})

# Current Game Render
def detail(request, board_id):
	try:
		# If we get a post request
		if request.method == 'POST':
			# Get params from POST request
			x = request.POST['x']
			y = request.POST['y']
			shift = request.POST['shift']
			# Get tile
			tile = Tile.objects.filter(board=board_id,
			 x=x, y=y)
			# if normal click
			if shift == 'off':
				reveal(board_id, x, y)
			# if shift and click
			if shift == 'on':
				tile[0].mark()
		# Get Board or throw 404 if not available
		board = get_object_or_404(Board, pk=board_id)
		# Get tiles
		tiles = Tile.objects.filter(board=board) # Cache tiles to not have to do this everytime
		# Render details page
		return render(request, 'game/detail.html', {'board': board, 'tiles': tiles})
	except Exception as inst:
		print inst
		

# Reveal tiles
def reveal(board_id, x, y):
	try:
		# Get tile
		tile = Tile.objects.filter(board=board_id,
		 x=x, y=y)
		# Reveal tile
		if tile[0].revealed == False:
			tile.update(revealed = True)
			x = int(x)
			y = int(y)
			# IF tile is blank uncover surrounding tiles
			if tile[0].mine == False and tile[0].value == 0:
				if x != 0:
					reveal(board_id, x-1, y)
				if x != 9:
					reveal(board_id, x+1, y)
				if y != 0:
					reveal(board_id, x, y-1)
				if y != 9:
					reveal(board_id, x, y+1)
	# Handle Exception
	except Exception as inst:
		print inst
		


