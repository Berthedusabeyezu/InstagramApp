from .models import Profile,Image,Comment,Like 
from django import forms


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [ 'pub_date']

class NewImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['profile', 'user']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment  
        exclude = ['user']

class LikeForm(forms.ModelForm):
    class Meta:
        model = Like
        exclude = ['user','image']    