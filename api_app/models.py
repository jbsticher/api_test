from django.db import models


class Songs(models.Model):
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Songs'

    def __str__(self):
        return self.title

