from django.db import models
from django.contrib.auth.models import User
from django.db.models .signals import post_save
from django.urls import reverse


# --------------  User Profile Model ----------------
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    phone_number = models.CharField(blank=True,max_length=13)
    image=models.ImageField(upload_to='profile/images',null=True,blank=True)
    def __str__(self):
        return f'{self.user.username}-{self.phone_number}'

# --------------  UserProfile signal  ----------------
def profile_save(sender ,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(profile_save,sender=User)

