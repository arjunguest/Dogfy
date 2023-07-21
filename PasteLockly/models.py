from django.db import models

class Snippet(models.Model):
    content = models.TextField()
    url = models.URLField(max_length=50, unique=True)
    secret_key = models.CharField(max_length=100, blank=True, null=True)
    encrypt = models.BooleanField(default = False)
    
    def __str__(self):
        return self.url
    class Meta:
        verbose_name_plural = "Snippet"