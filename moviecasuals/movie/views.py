from django.shortcuts import render

def add_movie(request):
    return render(request, 'movie/add_movie.html')