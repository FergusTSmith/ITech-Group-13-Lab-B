from django.db import models
from django.contrib.auth.models import User
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    city = models.CharField(max_length=3)
    logo = models.ImageField(upload_to='logo_images', blank=True)
    slug = models.SlugField(unique=True)

    like_help_jsons = models.CharField(max_length = 1000)

    like_quality_jsons = models.CharField(max_length=1000)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(LettingAgent, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    uniqueName = models.CharField(max_length=3, unique=True)
    picture = models.ImageField(upload_to='city_images', blank=True)
    description = models.CharField(max_length=500)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    #categories = models.CharField(max_length=50)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.uniqueName)
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.uniqueName

    class Meta:
        verbose_name_plural = 'Cities'

class LettingAgent(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    dateFounded = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    helpfulnessRating = models.IntegerField(default=0)
    promptnessRating = models.IntegerField(default=0)
    qualityRating = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    logo = models.ImageField(upload_to='logo_images', blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(LettingAgent, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Rental_Property(models.Model):
    NAME_MAX_LENGTH = 100
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    address = models.CharField(max_length=500, unique=True)
    description = models.CharField(max_length=500)
    picture = models.ImageField(upload_to='property_images/', blank=True)
    cleanlinessRating = models.IntegerField(default=0)
    accuracyRating = models.IntegerField(default=0)
    enjoyabilityRating = models.IntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    #city = models.CharField(max_length=3)
    lettingAgent = models.ForeignKey(LettingAgent, on_delete=models.CASCADE, null=True)
    #lettingAgent = models.CharField(max_length=20)
    price = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    state = models.BooleanField(default=True)
    followingUsers = models.ManyToManyField(User, null=True)

    objects = models.Manager()

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Rental_Property, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Rental_Properties'

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #username = models.CharField(max_length=30, unique=True)
    #email = models.CharField(max_length=128, unique=True)
    datejoined = models.DateField(auto_now_add=True)
    accessibleUser = models.BooleanField(default=False)
    superUser = models.BooleanField(default=False)
    profilePic = models.ImageField(upload_to='profile_images', blank=True)
    totallikes = models.IntegerField(default=0)
    totalComments = models.IntegerField(default=0)

    #isAgent = models.BooleanField(default=False)

    def __str__(self):
        return self.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Description = models.CharField(max_length=500)
    Date = models.DateField(auto_now_add=True)
    cleanlinessRating = models.IntegerField(default=0)
    accuracyRating = models.IntegerField(default=0)
    enjoyabilityRating = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

#https://www.gyford.com/phil/writing/2017/03/16/django-admin-map/

#https://stackoverflow.com/questions/71415953/keep-track-of-follow-unfollow-events-django
class UserFollows(models.Model):
    user = models.ManyToManyField(User)
    followedProperty = models.ManyToManyField(Rental_Property)
    followed = models.BooleanField(default=True)


