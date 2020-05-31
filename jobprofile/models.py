from django.db import models

class Jobprofile(models.Model):
    title_main= models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title
