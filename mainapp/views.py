from django.shortcuts import render,redirect
from django.http import HttpResponse
from mainapp .models import *
from .forms import *
def home(request):
    movie = Movie.objects.all()

    # context = {
    #     'movie':movie
    # }
    return render(request, 'mainapp/home.html',{'movie':movie})



def detaile(request,id):
    movies = Movie.objects.get(id=id)
    # context = {
    #     'movie':movie
    # }
    return render(request, 'mainapp/detailes.html', {'movie':movies})

    # add movie new 

def add_movies(request):
    if request.method == "POST":
        form = MovieForm(request.POST or None) 
        # check the data valid or not
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("home")
      
    else:
        form = MovieForm()

    return render(request, 'mainapp/addmovie.html',{"i":form,"controller" : "Add Movie"})


# edit the movie data

def edit_movies(request, id):
    # for movie link with id
    movie = Movie.objects.get(id = id)

    if request.method == "POST":
        form = MovieForm(request.POST or None, instance=movie)
        #form checking the area
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            return redirect("home")
    else:
        form = MovieForm(instance=movie)
    return render(request,'mainapp/addmovie.html',{"i":form,"controller" : "Edit Movie"})

 # delete the Movie

def delete_movie(request, id):
    # get the movie
    form = Movie.objects.get(id=id)

    #delete the movie

    form.delete()
    return redirect("home")
    return render(request, 'mainapp/detailes.html')