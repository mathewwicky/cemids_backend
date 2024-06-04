from django.db import models

class EducationalContent(models.Model):
    image = models.ImageField(upload_to='educational_images/', blank=True, null=True)
    author = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    description = models.TextField()
    readmore = models.URLField()

    def __str__(self):
        return self.subtitle
