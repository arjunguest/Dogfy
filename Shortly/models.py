from django.db import models

class Urls(models.Model):
    long_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.long_url
    class Meta:
        verbose_name_plural = "Urls"