from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=1000, default='')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
