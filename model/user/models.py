from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    description = models.TextField(max_length=500)
    create_data = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return str(self.name)

