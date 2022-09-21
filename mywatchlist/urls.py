from django.urls import path
from mywatchlist.views import show_mywatchlist
from mywatchlist.views import show_in_xml
from mywatchlist.views import show_movie_in_json

app_name = 'mywatchlist'

urlpatterns = [
    path('html/', show_mywatchlist, name='show_mywatchlist'),
    path('xml/', show_in_xml, name='show_in_xml'),
    path('json/', show_movie_in_json, name='show_movie_in_json'),
]