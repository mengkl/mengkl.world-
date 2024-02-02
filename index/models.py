from django.db import models


# Create your models here.


class Myapp(models.Model):
    my_apps_cn = models.CharField(blank=True, max_length=30)
    my_apps_en = models.CharField(blank=True, max_length=30)

    def __str__(self):
        return self.my_apps_en
