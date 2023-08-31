from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class LearningStyle(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


# User models that includes employee and employers
class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    class_level = models.CharField(max_length=10, blank=False, null=False)
    math_grade = models.CharField(max_length=10, blank=False, null=False)
    math_strength = models.CharField(max_length=10, blank=False, null=False)
    is_learning_style = models.BooleanField("Learning style",default=False)
    learning_style = models.ManyToManyField(LearningStyle)

    # log in with email instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    

