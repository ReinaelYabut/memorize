# chords_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.key_list, name='key_list'),
    path('key/<int:key_id>/', views.chord_list, name='chord_list'),
    path('add_key/', views.add_key, name='add_key'),
    path('add_chord/', views.add_chord, name='add_chord'),
    path('add_chord_image/', views.add_chord_image, name='add_chord_image'),
    path('flashcard_game/<int:key_id>/', views.flashcard_game, name='flashcard_game'),
    path('flashcard_data/<int:key_id>/', views.flashcard_data, name='flashcard_data'),

]
