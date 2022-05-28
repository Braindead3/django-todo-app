from django.db import models
from django.conf import settings
from django.utils import timezone


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    creation_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
