from django.shortcuts import render, get_object_or_404

from game.models import Game

def index(request):
    latest_game_list = Game.objects.all().order_by('-start_date')[:5]
    context = {'latest_game_list': latest_game_list}
    return render(request, 'game/index.html', context)

def detail(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    return render(request, 'game/detail.html', {'game': game})

def results(request, game_id):
    return HttpResponse("You're looking at the results of game %s." % game_id)

def turn(request, game_id):
    return HttpResponse("You're turn on game %s." % game_id)

# Create your views here.
