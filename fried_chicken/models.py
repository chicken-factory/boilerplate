from django.db import models
from django.conf import settings
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField(blank=True, null=True)
    
    def create(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

