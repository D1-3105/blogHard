from django.db import models


class Posts(models.Model):
    title = models.TextField()
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    text = models.TextField(max_length=20)
# Create your models here.
