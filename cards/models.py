from django.db import models
import datetime
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    name = models.CharField(max_length=30)
    user = models.OneToOneField(User, related_name='user')

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return self.name

    @classmethod
    def update_profile(cls, id, profile, update):
        new_profile = cls.objects.filter(id=id).update(profile=update)
        return new_profile


class Flashcard(models.Model):
    title = models.CharField(max_length=50)
    notes = models.TextField()
    profile = models.ForeignKey(Profile, null=True)
    image = models.ImageField(upload_to='images/', null=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)

    def save_flashcard(self):
        self.save()

    def delete_flashcard(self):
        self.delete()

    def __str__(self):
        return self.title

    @classmethod
    def update_flashcard(cls, id, flashcard, update):
        new_flashcard = cls.objects.filter(id=id).update(flashcard=update)
        return new_flashcard

    @classmethod
    def all_flashcards(cls):
        flashcards = cls.objects.all()
        return flashcards

    @classmethod
    def single_flashcard(cls, id):
        flashcard= cls.objects.get(id=id)
        return flashcard


class Course(models.Model):
    title = models.CharField(max_length=70)
    profile = models.ForeignKey(Profile, null=True)
    flashcards = models.ForeignKey(Flashcard, default='')

    def save_course(self):
        self.save()

    def delete_course(self):
        self.delete()

    def __str__(self):
        return self.title


    @classmethod
    def filter_by_course(cls, course):
        course = cls.objects.filter(course_id=course)
        return course

    class Meta:
        ordering = ['title']

    @classmethod
    def update_course(cls, id, course, update):
        new_course = cls.objects.filter(id=id).update(course=update)
        return new_course


class RegistrationReiepient(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
