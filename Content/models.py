from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Poll(models.Model):
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    option1 = models.CharField(max_length=25)
    option2 = models.CharField(max_length=25)
    option3 = models.CharField(max_length=25)
    votes1 = models.IntegerField(default=0)
    votes2 = models.IntegerField(default=0)
    votes3 = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Voted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)