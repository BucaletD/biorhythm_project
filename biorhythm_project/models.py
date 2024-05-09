from django.db import models

class UserProfile(models.Model):
    birthdate = models.DateField()
    # Add any other fields you need for user data
