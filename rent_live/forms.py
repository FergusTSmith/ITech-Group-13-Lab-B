from django.contrib.auth.models import User
from rent_live.models import UserProfile, LettingAgent, Rental_Property
from django import forms
from django.contrib.auth.forms import UserChangeForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('accessibleUser', 'profilePic')

class AgentProfileForm(forms.ModelForm):
    class Meta:
        model = LettingAgent
        fields = ('name', 'email', 'description', 'phone', 'city', 'logo', 'category', 'dateFounded')
        #https://www.youtube.com/watch?v=ke1IIHDwCIk
        #widgets = ('dateFounded', forms.DateInput(attrs='type':'date'))


class RentalPropertyForm(forms.ModelForm):
    class Meta:
        model = Rental_Property
        fields = ('name', 'address', 'description', 'picture', 'city', 'lettingAgent', 'price', 'size', 'state')

#https://www.youtube.com/watch?v=D9Xd6jribFU&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=19&ab_channel=MaxGoodridge
class ProfileEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('username', 'email',)
