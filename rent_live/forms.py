from django.contrib.auth.models import User
from rent_live.models import UserProfile, LettingAgent
from django import forms


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
        fields = ('name', 'description', 'phone', 'email', 'city', 'logo')