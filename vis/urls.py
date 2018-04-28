from django.urls import path

from . import views

urlpatterns = [
    # /vis/
	path('', views.index, name='index'),
	# ex: /vis/5/
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    # ex./vis/5/movie_results/
    path('<int:movie_id>/movie_results/', views.movie_results, name='movie_results'),
    # ex./vis/5/showtimes
    path('<int:movie_id>/showtimes/', views.showtimes, name='showtimes'),
]
