from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    profile_pic=models.ImageField(null=True,blank=True)
    profile_bio=models.TextField(max_length=300,null=True)
    def __str__(self):
        return self.user.username

class PicturePost(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    post_pic=models.ImageField(null=True,blank=True)
    post_topic=models.TextField(max_length=300,null=True)
    def __str__(self):
        return str(self.id)