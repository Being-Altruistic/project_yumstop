from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
import django
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # USer (1) - (M) posts | Foreign Key
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    bookmark = models.CharField(max_length=20, default="Null")
    def __str__(self):
        return self.title

class dieticians(models.Model):
    name = models.CharField(max_length=200)
    qualifications = models.TextField()
    ap = models.IntegerField()
    blogs = models.IntegerField()
    ratings=models.FloatField(default=0)
    tot_rank_score = models.FloatField(default=0)
    rank=models.IntegerField(default=0)
    bookmark = models.CharField(max_length=20, default="Null")
    def __str__(self):
        return self.name

class appointments(models.Model):
    consulter = models.CharField(max_length=200, default="Null")
    patient_id = models.IntegerField()
    patient_name = models.CharField(max_length=200, default="Null")
    desc=models.TextField(max_length=300, default="")
    patient_response = models.TextField(max_length=300, default="Null")
    status= models.CharField(max_length=200, default="")
    request_date = models.DateTimeField(default=django.utils.timezone.now)
    CLOSING = models.DateTimeField(default=timezone.now())
    treatment = models.TextField(max_length=300, default="Null")
    def __str__(self):
        return self.consulter