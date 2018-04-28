import datetime

from django.db import models
from django.utils import timezone

# Create your models here
class Theatre(models.Model):
    theatre_id = models.IntegerField(unique=True)
    theatre_name = models.CharField(max_length=200)
    address1 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    geo_long = models.DecimalField(max_digits=10,decimal_places=4, null=True)
    geo_lat = models.DecimalField(max_digits=10,decimal_places=4, null=True)
    theatre_name = models.CharField(max_length=100)
    theatre_url = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.theatre_name

class Movie(models.Model):
    movie_title = models.CharField(max_length=100)
    movie_id = models.IntegerField(unique=True)
    movie_genre = models.CharField(max_length=100, null=True)
    movie_poster = models.ImageField(max_length=100, null=True)
    movie_date = models.DateField('date released')
    movie_runtime = models.IntegerField()
    movie_stars = models.IntegerField(max_length=10,null=True)

    theatres = models.ManyToManyField(Theatre)

    def __str__(self):
        return self.movie_title
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Showtime(models.Model):
    showtime_id = models.IntegerField(max_length=100)
    showtime_date = models.DateField
    showtime_time = models.CharField(max_length=10)
    showtime_tickets = models.CharField(max_length = 250)

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theatre = models.ForeignKey(Theatre, on_delete=models.CASCADE)

    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.showtime_time + ' ' + self.movie.movie_title + ' ' + self.theatre.theatre_name
