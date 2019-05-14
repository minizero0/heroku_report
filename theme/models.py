from django.db import models

class Theme(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body= models.TextField()


# Create your models here.
