
from django.db import models
from django.utils import timezone

from passage.models import Passage


# Create your models here.
class Comments(models.Model):
    passage = models.ForeignKey(Passage, blank=True, null=True, on_delete=models.CASCADE, related_name='comments')

    comment = models.TextField()

    commentator = models.CharField(max_length=50)

    commentator_website = models.URLField(blank=True,null=True)

    created_time = models.DateTimeField(default=timezone.now)
