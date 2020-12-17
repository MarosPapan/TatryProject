from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class mountain(models.Model):
    mountain_name = models.CharField(max_length=60)
    #mountain_image = models.ImageField()

    def __str__(self):
        return self.mountain_name
class peaks(models.Model):
    name_of_mountain = models.ForeignKey(mountain, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    height = models.FloatField()
    location = models.CharField(max_length=200)
    gps = models.CharField(max_length=80)
    quick_description = models.CharField(max_length=94)
    text = models.TextField()

    def __str__(self):
        return self.name
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class posts(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts')
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.author.user} Post'

class texts_on_website(models.Model):
    where_text_is = models.CharField(max_length=500)
    text_on_website = models.TextField()

    def __str__(self):
        return self.where_text_is