from django.shortcuts import render
from .models import IgboAlphabet, IgboWord
from django.http import HttpResponse

# Create your views here.

def home(request):
    """
    Igbo Learning App – Home Page
    """ 
    return render(request, 'vocab/home.html')

def alphabet_list(request):
    alphabets = IgboAlphabet.objects.all()
    return render(request, 'vocab/alphabet_list.html', {'alphabets': alphabets})

def word_list(request):
    words = IgboAlphabet.objects.all()
    return render(request, 'vocab/word_list.html', {'words': words})