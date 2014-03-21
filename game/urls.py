from django.conf.urls import patterns, url

from game import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<game_id>\d+)/$', views.detail, name='detail'),
    # ex: /game/5/results/
    url(r'^(?P<game_id>\d+)/results/$', views.results, name='results'),
    # ex: /game/5/turn/
    url(r'^(?P<game_id>\d+)/turn/$', views.turn, name='turn'),
)