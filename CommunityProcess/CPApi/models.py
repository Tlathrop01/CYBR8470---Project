from django.db import models

# Create your models here.

class Issue(models.Model):
    Issue_name = models.CharField(max_length=25)
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.name