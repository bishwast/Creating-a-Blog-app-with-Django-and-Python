from django.db import models
from datetime import datetime

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    createdAt = models.DateTimeField(default=datetime.now, blank=True)  ## Save posts with a current date.