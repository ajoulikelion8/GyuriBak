from django.db import models
from django.utils import timezone
from user.models import User
# Create your models here.
class Post(models.Model):
    name = models.ForeignKey (User, on_delete=models.CASCADE, blank =True, null=True)
    title = models.CharField(max_length=50)
    body = models.TextField(max_length = 500)
    publish_date = models.DateTimeField(default = timezone.now)
    objects = models.Manager()

    def __str__(self):
        return str(self.title)