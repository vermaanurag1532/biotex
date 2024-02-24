from django.db import models

# Create your models here.


class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    image = models.ImageField(upload_to='uploads/team')
    designation = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name
    
class Career(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    date = models.DateField()
    link = models.URLField(default='NA')