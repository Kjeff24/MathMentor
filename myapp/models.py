from django.db import models
from django.contrib.auth.models import AbstractUser


# User models that includes employee and employers
class User(AbstractUser):
    is_email_verified = models.BooleanField(default=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
    class_level = models.CharField(max_length=10, blank=False, null=False)
    math_grade = models.CharField(max_length=10, blank=False, null=False)
    math_strength = models.CharField(max_length=10, blank=False, null=False)
    has_preference = models.BooleanField("Has Preference",default=False)
    is_auditory_learner = models.BooleanField("Auditory Learner",default=False)
    is_visual_learner = models.BooleanField("Visual Learner",default=False)
    is_kinesthetic_learner = models.BooleanField("Kinesthetic Learner",default=False)
    is_read_write_learner = models.BooleanField("Read/Write Learner",default=False)

    # log in with email instead of username
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
    

