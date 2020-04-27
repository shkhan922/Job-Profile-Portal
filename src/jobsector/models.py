from django.db import models

class Jobsector(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    thumbnail = models.ImageField()

    def __str__(self):
        return self.title
