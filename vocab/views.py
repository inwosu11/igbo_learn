from django.shortcuts import redirect, render, get_object_or_404
from .models import IgboAlphabet, IgboWord
from django.http import HttpResponse
from .forms import IgboWordForm
import random

# Create your views here.

def home(request):
    """
    Igbo Learning App – Home Page
    """ 
    return render(request, 'vocab/home.html')

def alphabet_list(request):
    alphabets = IgboAlphabet.objects.all()
    return render(request, 'vocab/alphabet_list.html', {'alphabets': alphabets})

def flashcards(request):
    words = list(IgboWord.objects.all())[:10]  # Get first 10 words for flashcard
    random.shuffle(words) #optional: shuffle for randomness
    return render(request, 'vocab/flashcards.html', {'words': words})

def word_list(request):
    words = IgboWord.objects.prefetch_related('dialect_words').all()
    return render(request, 'vocab/word_list.html', {'words': words})

def create_igbo_word(request):
    if request.method == 'POST':
        form = IgboWordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('word_list')
    else:
        form = IgboWordForm()
    
    return render(request, 'vocab/create_word.html', {'form': form})

def word_detail(request, slug):
    word = get_object_or_404(IgboWord.objects.prefetch_related('dialect_words'), slug=slug)
    return render(request, 'vocab/word_detail.html', {'word':word})