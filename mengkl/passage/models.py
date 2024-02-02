from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField


# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Passage(models.Model):
    title = models.CharField(max_length=100, blank=True)

    created_time = models.DateTimeField(default=timezone.now)

    author = models.CharField(max_length=50, blank=True)

    body = MDTextField()

    pid = models.PositiveIntegerField(unique=True)

    abstract = MDTextField(blank=True, null=True)
    abstract_after_changed = models.TextField(blank=True, null=True)

    tags = models.ManyToManyField(Tag, related_name='passages')

    absimg = models.URLField(blank=True)

    def __str__(self):
        return self.title
