from django.shortcuts import render

def add_director(request):
    return render(request, 'director/add_director.html')