from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('Scrabble_Aid', views.Scrabble_Aid),
    path('Word_Cookie_Aid', views.Word_Cookie_Aid),
]
