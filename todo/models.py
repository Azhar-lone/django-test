from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=100)  # Task title (text field with max 100 characters)
    description = models.TextField(blank=True)  # Task description (optional)
    is_completed = models.BooleanField(default=False)  # Whether the task is done
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp when the task was created

    def __str__(self):
        return self.title
