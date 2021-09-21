from django.core.files import storage
from django.db import models
# from django.core.files.storage import FileSystemStorage
from django_jsonfield_backport.models import JSONField

# Create your models here.

# fs = FileSystemStorage(location='/media/photos')

class Post(models.Model):
  who_posted = models.CharField(max_length=200, null=True)
  approved = models.BooleanField(default=False, null=True)
  image = models.ImageField(default="image.png", null=True)
  likes = models.IntegerField(default=0, null=True)
  liked_by = JSONField(default=list, null=False)
  comments = JSONField(default=list, null=False)

  def __str__(self):
    return self.who_posted


