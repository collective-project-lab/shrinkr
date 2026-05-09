from .base import BaseStorage
from core.models import ShortenedURL


class SQLiteStorage(BaseStorage):

    def save(self, long_url: str) -> str:
        obj = ShortenedURL.objects.create(long_url=long_url)
        return obj.short_code

    def get(self, short_code: str) -> str | None:
        try:
            obj = ShortenedURL.objects.get(short_code=short_code)
            obj.click_count += 1
            obj.save()
            return obj.long_url
        except ShortenedURL.DoesNotExist:
            return None

    def delete(self, short_code: str) -> bool:
        try:
            ShortenedURL.objects.get(short_code=short_code).delete()
            return True
        except ShortenedURL.DoesNotExist:
            return False

    def list_all(self) -> list:
        return list(
            ShortenedURL.objects.values(
                'short_code', 'long_url', 'created_at', 'click_count'
            ).order_by('-created_at')
        )