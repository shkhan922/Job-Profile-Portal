from django.db import models

# Model for the Job Sector 
class Jobsector(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    thumbnail = models.ImageField()
    featured = models.BooleanField()

    def __str__(self):
        return self.title
