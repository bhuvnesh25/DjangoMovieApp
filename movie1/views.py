from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse
from.models import Movie
from django .template import loader



def index(request):
    all_movies=Movie.objects.all()
    template=loader.get_template('movie1/index.html')
    context={
        'all_movies':all_movies

    }
    return HttpResponse(template.render(context,request))

def detail(request,movie_id):
    return HttpResponse("<h1>welcome in id :" + str(movie_id) + "</h1>")