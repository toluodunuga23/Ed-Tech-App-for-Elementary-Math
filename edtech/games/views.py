from django.shortcuts import render
from django.http import HttpResponse

from tkinter import *
from random import randint
from .models import *

def games(request):
    return render(request,"home.html")


def signup(request):
    return render(request,"signup.html")


# Flashcard 
def flashcards(request):

    return render(request, 'flashcards.html')

def createflashcards(request):
    if request.method == 'POST':
        term = request.POST['term']
        definition = request.POST['definition']
        flashcard = createFlashcards(term=term, definition=definition)
        flashcard.save()
        return render(request, 'flashcards.html')
   



