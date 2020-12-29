# from django.contrib.auth.models import User
from .models import UserProfile,PicturePost
from django.forms import forms,ModelForm

# user profile form 
class UserProfileForm(ModelForm):
    class Meta:
        model=UserProfile
        fields={'profile_bio','profile_pic'}

# user post form
class UserPostForm(ModelForm):
    class Meta:
        model=PicturePost
        fields={'post_pic','post_topic'}
