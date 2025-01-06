from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class MisakaMikoto(models.Model):
    name = models.CharField(max_length=128)
    age = models.IntegerField(default=0)
    email = models.EmailField(max_length=254, unique=True, default="example@example.com")

    def __str__(self):
        return self.name

class Webpage(models.Model):
    topic = models.ForeignKey(MisakaMikoto, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    url = models.URLField()

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)

class users(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=254, unique=True, default="example@example.com")

    def __str__(self):
        return self.name
    
# for user authentication
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional classes
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)

    def __str__(self):
        return self.user.username