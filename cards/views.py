from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Flashcard, Profile, Course
import datetime

# Create your views here.
def index(request):
    profile = Profile.objects.all()
    flashcards = Flashcard.objects.all()
    courses = Course.objects.all()

    args = {'profile':profile, 'flashcards': flashcards, 'courses':courses}

    return render(request, 'index.html', args)

def flashcard(request, pk):
    flashcard = Flashcard.objects.get(pk=pk)
    return render(request, 'flashcard.html', args)