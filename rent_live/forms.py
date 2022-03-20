from django.contrib.auth.models import User
from rent_live.models import UserProfile, LettingAgent, Rental_Property, UserMessage, PropertyComment, AgentComment
from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

# Form to allow the users to sign up. This is sourced from Tango With Django page 156 - retrieved 10/03/2022
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

# Form that allows users to sign up with additional details. This is adapted from Tango With Django page 156 - retrieved 10/03/2022
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('accessibleUser', 'profilePic')

# Form that allows the user to register as a LettingAgent
class AgentProfileForm(forms.ModelForm):
    class Meta:
        model = LettingAgent
        fields = ('name', 'description', 'phone', 'city', 'logo', 'category')

# Form that allows letting agents to register a new property.
class RentalPropertyForm(forms.ModelForm):
    class Meta:
        model = Rental_Property
        fields = ('name', 'address', 'description', 'picture', 'city', 'lettingAgent', 'price', 'size', 'Ready')

# This form allows users to edit their profile. This was adapted from a youtube tutoial by Max Goodridge - Retrieved 17/03/2022 - https://www.youtube.com/watch?v=D9Xd6jribFU&list=PLw02n0FEB3E3VSHjyYMcFadtQORvl1Ssj&index=19&ab_channel=MaxGoodridge
class ProfileEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('username', 'email',)

# Form allows users to create a new message for another user
class UserMessageForm(forms.ModelForm):
    class Meta:
        model = UserMessage
        fields = ('recepient', 'subject', 'detail',)

# Form allows users to comment on a rental property
class RentalPropertyComment(forms.ModelForm):
    class Meta:
        model = PropertyComment
        fields = ('Description', 'property', 'cleanlinessRating', 'accuracyRating', 'enjoyabilityRating')

# From allows users to comment on a letting agent page.
class LettingAgentComment(forms.ModelForm):
    class Meta:
        model = AgentComment
        fields = ('Description', 'agent', 'promptnessRating', 'helpfulnessRating', 'qualityRating')