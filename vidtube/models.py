from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime,timedelta
from django.utils import timezone
# Create your models here.
User=get_user_model()

class account(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,)
    id_user=models.IntegerField()
    dp=models.ImageField(upload_to=r'C:\Users\sures\OneDrive\Documents\python\django\youtube_clone\media',default='tom.png')
    subscribers=models.IntegerField(default=0)
    
class post(models.Model):
    id=models.UUIDField(default=uuid.uuid4,primary_key=True)
    user=models.ForeignKey(account,on_delete=models.CASCADE)
    title=models.CharField(max_length=50,blank=True)
    #dp=models.ImageField(upload_to=r'C:\Users\sures\OneDrive\Documents\python\django\youtube_clone\media',default='tom.png')
    thumb=models.ImageField(upload_to=r'C:\Users\sures\OneDrive\Documents\python\django\youtube_clone\media',default='thumbnail1.png')
    dat=models.DateTimeField(default=datetime.now)
    likes=models.IntegerField(default=0)
    des=models.CharField(max_length=150,blank=True)
    views=models.IntegerField(default=0)
    sub=models.IntegerField(default=0)
    def datdif(self):
        c=-(timezone.now()-self.dat).total_seconds()
        return str(c)+"seconds"
    class Meta:
        ordering=['?']
class subcribe(models.Model):
    user=models.CharField(max_length=50)
    acc_id=models.CharField(max_length=150)
class like(models.Model):
    user=models.CharField(max_length=50)
    acc_id=models.CharField(max_length=150)
class view(models.Model):
    user=models.CharField(max_length=50)
    vid_id=models.CharField(max_length=150)
class comment(models.Model):
    user=models.ForeignKey(account,on_delete=models.CASCADE)
    # user=models.CharField(max_length=50)
    vid_id=models.CharField(max_length=150)
    comments=models.CharField(max_length=500)
    at=models.DateTimeField(default=datetime.now)