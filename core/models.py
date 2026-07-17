from django.db import models
import random
import string
from .utils import encode_id


class ShortenedURL(models.Model):
    long_url    = models.URLField()
    short_code  = models.CharField(max_length=10, unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    click_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        is_new_instance = self.pk is None
        super().save(*args, **kwargs)

        if is_new_instance and not self.short_code:
            self.short_code = encode_id(self.pk)
            super().save(update_fields=['short_code'])

    def __str__(self):
        return f"{self.short_code} → {self.long_url}"