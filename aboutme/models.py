from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.

class AboutMe(models.Model):
    title = models.CharField(max_length=50)
    body = MDTextField()
    body_after_changed = models.TextField(blank=True, null=True)
