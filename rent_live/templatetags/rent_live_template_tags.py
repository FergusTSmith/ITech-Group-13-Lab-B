# TWD pg 144
from django import template
from rent_live.models import City

register = template.Library()

@register.inclusion_tag('rent_live/cities.html')
def get_all_cities():
    allCities = {'cities': City.objects.all()}
    return allCities