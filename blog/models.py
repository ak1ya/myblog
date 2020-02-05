from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    last_modify = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title