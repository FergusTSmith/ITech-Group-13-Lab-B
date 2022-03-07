from django.db import models

# Create your models here.
from django.template.defaultfilters import slugify

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class LettingAgent(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    dateFounded = models.DateField
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    helpfulnessRating = models.IntegerField(default=0)
    promptnessRating = models.IntegerField(default=0)
    qualityRating = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    city = models.CharField(max_length=3)
    logo = models.ImageField(upload_to='logo_images', blank=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    uniqueName = models.CharField(max_length=3, unique=True)
    picture = models.ImageField(upload_to='city_images', blank=True)
    description = models.CharField(max_length=500)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.uniqueName

    class Meta:
        verbose_name_plural = 'Cities'

class Rental_Property(models.Model):
    NAME_MAX_LENGTH = 100
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    address = models.CharField(max_length=500, unique=True)
    description = models.CharField(max_length=500)
    picture = models.ImageField(upload_to='property_images', blank=True)
    cleanlinessRating = models.IntegerField()
    accuracyRating = models.IntegerField()
    enjoyabilityRating = models.IntegerField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    lettingAgent = models.ForeignKey(LettingAgent, on_delete=models.CASCADE)
    price = models.IntegerField()
    size = models.IntegerField()
    followers = models.IntegerField(default=0)
    state = models.BooleanField()

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Rental_Property, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Rental_Properties'

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=128, unique=True)
    datejoined = models.DateField(auto_now_add=True)
    accessibleUser = models.BooleanField(default=False)
    superUser = models.BooleanField(default=False)
    profilePic = models.ImageField(upload_to='profile_images', blank=True)
    totallikes = models.IntegerField(default=0)
    totalComments = models.IntegerField(default=0)

    def __str__(self):
        return self.username

class Comment(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Description = models.CharField(max_length=500)
    Date = models.DateField(auto_now_add=True)
    cleanlinessRating = models.IntegerField()
    accuracyRating = models.IntegerField()
    enjoyabilityRating = models.IntegerField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.User

