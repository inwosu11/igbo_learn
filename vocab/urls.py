from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), #maps to home page /
    path('alphabet/', views.alphabet_list, name='alphabet_list'), #/alphabet/
    path('words/', views.word_list, name='word_list'), #/words/
    path('add-word/', views.create_igbo_word, name='add_word'),
    path('words/<slug:slug>/', views.word_detail, name='word_detail'),
    path('flashcards/', views.flashcards, name='flashcards'),
    path('flashcards/practice/', views.practice_flashcards, name='practice_flashcards'),
]
