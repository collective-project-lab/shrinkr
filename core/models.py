from django.db import models
import random
import string


def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choices(chars, k=length))
        if not ShortenedURL.objects.filter(short_code=code).exists():
            return code


class ShortenedURL(models.Model):
    long_url    = models.URLField()
    short_code  = models.CharField(max_length=10, unique=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    click_count = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = generate_short_code()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} → {self.long_url}"