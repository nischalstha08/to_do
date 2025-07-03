from django.db import models
<<<<<<< HEAD
=======

>>>>>>> 652cf96 (changes made to ui and also changed the edit and update)
from django.utils import timezone

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    is_completed = models.BooleanField(default=False)
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title