from django.http import HttpResponse


def index(request):
    movies_list = Movie.objects.order_by('-movie_date')[:5]
    template = loader.get_template('vis/index.html')
    context = {
        'movies_list':movies_list,
    }
    return HttpResponse(template.render(context, request))

def movie_detail(request, movie_id):
    return HttpResponse("You're looking at movie %s." % movie_id)
def movie_results(request, movie_id):
    response = "You're looking at the results of theatres %s."
    return HttpResponse(response % movie_id)

#def theatre_detail(request, movie_id):
#    response = "You're looking at the results of theatres %s."
#    return HttpResponse(response % theatre_id)

def showtimes(request, movie_id):
    response = "Here you can see an analysis of how many movies play at a certian time. &s"
    return HttpResponse(response % movie_id)
