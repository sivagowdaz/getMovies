from django.urls import path
from .views import getNewMovie, getKannadaMovie 
urlpatterns = [
    path('', getNewMovie, name='home'),
    path('movies', getKannadaMovie, name='movies'),
]
