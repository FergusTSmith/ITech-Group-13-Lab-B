from django.contrib import admin

# Register your models here.
from django.contrib import admin
from rent_live.models import Category, LettingAgent, City, Rental_Property, User, Comment, UserProfile

admin.site.register(Category)
admin.site.register(LettingAgent)
admin.site.register(City)
admin.site.register(Rental_Property)
#admin.site.register(User)
admin.site.register(Comment)
admin.site.register(UserProfile)

#https://django-map-widgets.readthedocs.io/en/latest/widgets/point_field_map_widgets.html



