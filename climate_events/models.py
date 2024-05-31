from django.db import models

class ClimateEvent(models.Model):
    event_title = models.CharField(max_length=200)
    event_description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__(self):
        return self.event_title
