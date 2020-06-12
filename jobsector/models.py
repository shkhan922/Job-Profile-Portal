from django.db import models

# Model for Job Category
class Jobcategory(models.Model):
    title = models.CharField(max_length=30)
    overview = models.TextField()
    thumbnail = models.ImageField()
    featured = models.BooleanField()

    def __str__(self):
        return self.title

# Model for the Job Sector 
class Jobsector(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    thumbnail = models.ImageField()
    featured = models.BooleanField()
    category = models.ManyToManyField(Jobcategory)


    def __str__(self):
        return self.title

# Model for Job Profile

class Jobprofile(models.Model):
    title = models.CharField(max_length=100)
    summary = models.TextField()
    job_description = models.TextField()
    salary = models.TextField()
    responsibilties = models.TextField()
    qualification = models.TextField()
    skills = models.TextField()
    hiring = models.TextField()
    Coaching_institution = models.TextField()
    locations = models.TextField()
    featured = models.BooleanField()

    def __str__(self):
        return self.title