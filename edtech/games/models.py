from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    bio= models.TextField(max_length=500, blank=True)
    profileimg= models.ImageField(upload_to='profile_images', default='blank-profile-picture.png')
    location = models.CharField(max_length=30, blank=True)
    school_year= models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.user.username



class createFlashcards(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question
   

