from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome To My Recipes App!</h1>")

def about(request):
    return HttpResponse("<h1>About My Recipes App!</h1>")
