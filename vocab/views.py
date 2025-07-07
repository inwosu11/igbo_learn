from django.shortcuts import redirect, render
from .models import IgboAlphabet, IgboWord
from django.http import HttpResponse
from .forms import IgboWordForm
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
    words = IgboWord.objects.prefetch_related('dialectword_set').all()
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
