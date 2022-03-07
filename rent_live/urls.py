from django.urls import path
from rent_live import views

app_name = 'rent_live'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index')
]