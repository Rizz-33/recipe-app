from django.shortcuts import render, HttpResponse
from . import models


def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/home.html', context)

def about(request):
    return render(request, 'recipes/about.html', {'title': 'About Us'})
