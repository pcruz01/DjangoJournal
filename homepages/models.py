from django.db import models

# Create your models here.
class EntryCategory(models.Model):
    description = models.CharField(max_length=20)
    

    def __str__(self):
        return (self.description)