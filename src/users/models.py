from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def user_profile_path(instance, filename):
    return 'user/{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)  
    #OneToOneField => bir kullanıcıya bir profil
    #on_delete=models.CASCADE => kullanıcı silinirse ona ait  profil de silisin
    image = models.ImageField(upload_to=user_profile_path , default = "user_icon.png")
    bio = models.TextField(blank=True) #blank=True => doldurulması zorunlu olmayan text
    
    def __str__(self):
        return "{} {}".format(self.user, 'Profile')