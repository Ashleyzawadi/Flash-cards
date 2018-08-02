from django.contrib import admin
from .models import Flashcard, Profile, Course

# Register your models here.
admin.site.register(Flashcard)
admin.site.register(Profile)
admin.site.register(Course)

