from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from game.models import Board, Tile

def index(request):
	newboard = Board.objects.create(width=10, 
		height=10, numberOfMines=25)
	board = get_object_or_404(Board, pk=newboard.id)
	for x in range(0, newboard.width):
		for y in range(0, newboard.height):
			tile = Tile.objects.create(board=board, mine=False, revealed=False, marked=False, value=False, x=x, y=y)
	return render(request, 'game/detail.html', {'board': board})

def detail(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    return render(request, 'game/detail.html', {'board': board})

def results(request, board_id):
    return HttpResponse("You're looking at the results of board %s." % board_id)

def turn(request, board_id):
    return HttpResponse("You're turn on board %s." % board_id)

# Create your views here.
