from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=50 ,blank=False,null=False)
    body = models.TextField(max_length=300,blank=False,null=False)
    models.ImageField(blank=True)

    def __str__(self):
        return self.name