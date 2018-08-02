from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Flashcard, Profile, Course
import datetime

# Create your views here.
@login_required
def index(request):
    profile = Profile.objects.all()
    flashcards = Flashcard.objects.all()
    courses = Course.objects.all()

    args = {'profile':profile, 'flashcards': flashcards, 'courses':courses}

    return render(request, 'index.html', args)

def flashcard(request, flashcard_id):
    flashcard = Flashcard.objects.get(pk=flashcard_id)
    args = {'flashcard': flashcard}
    return render(request, 'flashcard.html', args)
