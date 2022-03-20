from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Use of validators to create maximum and minimum values is adapted from (retrieved 20/03/2022) https://stackoverflow.com/questions/849142/how-to-limit-the-maximum-value-of-a-numeric-field-in-a-django-model
# Create your models here.
from django.template.defaultfilters import slugify

# Category - Different types for letting agents (I.e., agent, landlord, or agency)
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
 
# City Model stores information for cities that have been registered on RentLive
class City(models.Model):
    name = models.CharField(max_length=50)
    uniqueName = models.CharField(max_length=3, unique=True)
    picture = models.ImageField(upload_to='city_images', blank=True)
    description = models.CharField(max_length=500)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.uniqueName)
        super(City, self).save(*args, **kwargs)

    def __str__(self):
        return self.uniqueName

    class Meta:
        verbose_name_plural = 'Cities'

# Letting Agent model for the individual entities. 
class LettingAgent(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    dateJoined = models.DateField(auto_now_add=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    helpfulnessRating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    promptnessRating = models.IntegerField(default=0,  validators=[MaxValueValidator(10), MinValueValidator(0)])
    qualityRating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    totalHelpfulness = models.IntegerField(default=0)
    totalPromptness = models.IntegerField(default = 0)
    totalQuality = models.IntegerField(default=0)
    totalRatings = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    logo = models.ImageField(upload_to='logo_images', blank=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(LettingAgent, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

# This model stores information on the individual properties that have been posted to RentLive
class Rental_Property(models.Model):
    NAME_MAX_LENGTH = 100
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    address = models.CharField(max_length=500, unique=True)
    description = models.CharField(max_length=500)
    picture = models.ImageField(upload_to='property_images/', blank=True)
    cleanlinessRating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    accuracyRating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    enjoyabilityRating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    totalCleanliness = models.IntegerField(default=0)
    totalAccuracy = models.IntegerField(default =0)
    totalEnjoyability = models.IntegerField(default =0)
    totalRatings = models.IntegerField(default=0)
    city = models.ForeignKey(City, on_delete=models.CASCADE, null=True)
    lettingAgent = models.ForeignKey(LettingAgent, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(default=0)
    size = models.IntegerField(default=0)
    followers = models.IntegerField(default=0)
    Ready = models.BooleanField(default=True)
    followingUsers = models.ManyToManyField(User)

    longitude = models.CharField(max_length=255, blank=True)
    latitude = models.CharField(max_length=255, blank=True)

    objects = models.Manager()

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Rental_Property, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Rental_Properties'

    def __str__(self):
        return self.name

# This information contains additional information to the User default model and allows us to store more details for users.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    datejoined = models.DateField(auto_now_add=True)
    accessibleUser = models.BooleanField(default=False)
    superUser = models.BooleanField(default=False)
    profilePic = models.ImageField(upload_to='profile_images', blank=True)
    totallikes = models.IntegerField(default=0)
    totalComments = models.IntegerField(default=0)


    def __str__(self):
        return self.username

# This model stores information for comments left on a rental property
class PropertyComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Author")
    property = models.ForeignKey(Rental_Property, on_delete=models.CASCADE)
    uniqueID = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=500)
    Date = models.DateField(auto_now_add=True)
    cleanlinessRating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    accuracyRating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    enjoyabilityRating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    likes = models.IntegerField(default=0)
    likingUsers = models.ManyToManyField(User, related_name="Likers")
    userHasNotLiked = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

# This model stores information on comments left on an Agent page
class AgentComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="AgentAuthor")
    agent = models.ForeignKey(LettingAgent, on_delete=models.CASCADE)
    uniqueId = models.AutoField(primary_key=True)
    Description = models.CharField(max_length=500)
    Date = models.DateField(auto_now_add=True)
    promptnessRating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    qualityRating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    helpfulnessRating = models.IntegerField(default=0, validators=[MaxValueValidator(10), MinValueValidator(0)])
    likes = models.IntegerField(default=0)
    likingUsers = models.ManyToManyField(User, related_name="AgentLikers")
    userHasNotLiked = models.BooleanField(default=True)

# This model stores information on messages sent from one user to another.
class UserMessage(models.Model):
    recepient = models.ForeignKey(User, on_delete=models.CASCADE, related_name="MessageRecepient")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="MessageAuthor")
    subject = models.CharField(max_length=100)
    detail = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
