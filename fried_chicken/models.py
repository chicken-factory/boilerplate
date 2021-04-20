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

class Content(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    attachments = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
