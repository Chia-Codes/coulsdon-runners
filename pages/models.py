from django.db import models


class Page(models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=120)
    body = models.TextField(blank=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
