from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.TextField(default='untitled')
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    to_completed = models.BooleanField(default=False)
    def __str__(self):
        return self.title
