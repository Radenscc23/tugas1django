from django.shortcuts import render
from mywatchlist.models import filmWatchlist
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    data_film_watchlist = filmWatchlist.objects.all()
    context = {
    'list_film': data_film_watchlist,
    'nama': 'Raden D'
}
    return render(request, "mywatchlist.html", context)

def show_in_xml(request):
    data = filmWatchlist.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_movie_in_json(request):
    data = filmWatchlist.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    
# Create your views here.
