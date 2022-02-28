from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify

class Rental_Property(models.model):
    NAME_MAX_LENGTH = 100
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    address = models.CharField(max_length=500, unique=True)
    description = models.CharField(max_length=500)
    # Pictures
    cleanlinessRating = models.IntegerField(max=5)
    accuracyRating = models.IntegerField(max=5)
    enjoyabilityRating = models.IntergerField(max=5)
    city = models.CharField(max_length=3)
    lettingAgent = models.CharField(max_length=50)
    price = models.IntegerField()
    size = models.IntegerField()
    followers = models.IntegerField()
    state = models.BooleanField()

    slug = models.slugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(RentalProperty, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Rental_Properties'

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    User = models.CharField(max_length=128)
    Description = models.CharField(max_length=500)
    Date = models.DateField()
    cleanlinessRating = models.IntegerField(max=5)
    accuracyRating = models.IntegerField(max=5)
    enjoyabilityRating = models.IntegerField(max=5)
    likes = models.IntegerField(default=0)

class User(models.Model):
    username = models.CharField(max_length=30, unqiue=True)
    email = models.CharField(max_length=128)
    datejoined = models.DateField
    accessibleUser = models.BooleanField(default=False)
    superUser = models.BooleanField(default=False)
    # Profile Pic
    totallikes = models.IntegerField(default=0)
    totalComments = models.IntegerField(default=0)

class City(models.Model):
    name = models.CharField(50)
    uniqueName = models.Charfield(max_length=3, unique=True)
    # City Picture
    description = models.CharField(max_length=500)
    categories = models.CharField()

class LettingAgent(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    dateFounded = models.DateField
    phone = models.CharField(max_length=15)
    email = modles.CharField(max_length=50)
    helpfulnessRating = models.IntegerField(max=5)
    promptnessRating = models.IntegerField(max=5)
    qualityRating = models.IntegerField(max=5)
    category = models.CharField(max_length=20)
    city = models.CharField(max_length=3)
    # Logo
