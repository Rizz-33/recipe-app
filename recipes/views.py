from django.shortcuts import render, HttpResponse
from . import models

recipes = [
    {
        'author': 'Risini',
        'title': 'Chicken Pie',
        'direction': 'Add more chicken pieces with cheese',
        'date_posted': 'May 12 2024'
    },
    {
        'author': 'Dulaj',
        'title': 'Pizza',
        'direction': 'Add cheese, pepperoni and other stuff',
        'date_posted': 'May 11 2024'
    },
    {
        'author': 'Thamara',
        'title': 'Cheese Cake',
        'direction': 'Mix cheese and butter',
        'date_posted': 'May 10 2024'
    }
]

def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/home.html', context)

def about(request):
    return render(request, 'recipes/about.html', {'title': 'About Us'})
