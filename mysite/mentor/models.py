from django.db import models


class About(models.Model):
    title = models.CharField(max_length=250, blank=False, null=False)
    description = models.CharField(blank=False, null=False)
    image = models.ImageField(upload_to='images/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
