from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    
    bio = models.CharField(max_length=50)
    image = models.ImageField(upload_to = 'images/')
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.profile_photo

    def save_profile(self):
        self.save()  
    
    def delete_profile(self):
        self.delete()
       
    def update_profile(self, update):
        self.profile_photo = update 
        self.save()
    
    
class Image(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =60)
    caption = models.TextField()

    def __str__(self):
        return self.image

    
    def save_image(self):
        self.save()  

    @classmethod
    def get_images(cls):
        Image.objects.all()
    
    def update_caption(self, update):  
        self.image = update 
        self.save()


    def delete_image(self):
        self.delete()
          
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    comment = models.CharField(max_length =60)
   

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'images/')
    likes= models.IntegerField(default=0)
    
    def __str__(self):
        return self.likes

    def save_likes(self):
        self.save()

