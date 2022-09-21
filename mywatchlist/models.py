from django.db import models

class filmWatchlist(models.Model):
    watchedmovies = models.BooleanField(max_length=50)
    titlemovie = models.TextField()
    ratingmovie = models.IntegerField()
    moviereleasedate = models.TextField()
    reviewmovie = models.TextField()
    
    
# Create your models here.
