from django.urls import path
from . import views

'app/model_viewtypes'
'recipes/recipe_detail.html'

urlpatterns = [
    path('', views.RecipeListView.as_view(), name='recipes-home'),
    path('recipe/<int:pk>', views.RecipeDetailView.as_view(), name='recipes-detail'),
    path('about/', views.about, name='recipes-about'),
]
