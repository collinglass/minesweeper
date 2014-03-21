from django.conf.urls import patterns, url

from game import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<board_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<board_id>\d+)/results/$', views.results, name='results'),
    url(r'^(?P<board_id>\d+)/turn/$', views.turn, name='turn'),
)