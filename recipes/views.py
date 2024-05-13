from django.shortcuts import render, HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from . import models


def home(request):
    recipes = models.Recipe.objects.all()
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/home.html', context)

class RecipeListView(ListView):
    model = models.Recipe
    template_name ='recipes/home.html'
    context_object_name ='recipes'

class RecipeDetailView(DetailView):
    model = models.Recipe

class RecipeCreateView(LoginRequiredMixin,CreateView):
    model = models.Recipe
    fields = ['title', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class RecipeUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = models.Recipe
    fields = ['title', 'description']

    def test_func(self):
        recipe = self.get_object()
        if self.request.user == recipe.author:
            return True
        return False

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'recipes/about.html', {'title': 'About Us'})
