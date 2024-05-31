from django.db import models

class ProfileSettings(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    first_name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phonenumber = models.CharField(max_length=15)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    nationality = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    job_title = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.surname}"

