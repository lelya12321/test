from django.db import models

# Create your models here.
#
from django.db import models

class MyModel(models.Model):

    x = models.CharField(max_length=100)

    def __str__(self):
        return self.x