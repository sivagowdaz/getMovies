from django.urls import path
from .views import getNewMovie, getKannadaMovie , downloadMovie
urlpatterns = [
    path('', getNewMovie, name='home'),
    path('movies', getKannadaMovie, name='movies'),
    path('testing', downloadMovie, name='download movie')
]
