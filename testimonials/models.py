from django.db import models


class Testimonial(models.Model):
    author = models.CharField(max_length=120)
    quote = models.TextField()
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.author}: {self.quote[:30]}..."
