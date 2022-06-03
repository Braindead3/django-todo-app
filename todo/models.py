from django.db import models
from django.conf import settings
from django.utils import timezone


class Group(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    creation_time = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    complete = models.BooleanField(default=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
