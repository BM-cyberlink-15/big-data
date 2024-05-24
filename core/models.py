from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_TYPES = (
        ('Male', 'male'),
        ('Female', 'female')
    )

    local_address = models.CharField(max_length=255, blank=True, null=True)
    foreign_address = models.CharField(max_length=255, blank=True, null=True)
    gender = modes.CharField(max_length=6, choices=GENDER_TYPES, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    



class Channels(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'channel'
        verbose_name = 'channel'
        verbose_name_plural = 'channels'

    def __str__(self):
        return self.name


class UserChannel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channels, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    video = models.SmallIntegerField()
    followers = models.SmallIntegerField()
    views = models.SmallIntegerField()
    comment = models.SmallIntegerField()
    country = models.CharField(max_length=100)
    created_date = models.DateField()

    class Meta:
        db_table = 'user_channel'
    
    def __str__(self):
        return f'{self.user} ==> {self.channel}'