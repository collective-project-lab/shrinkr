import json
import redis
from django.conf import settings
from .base import BaseStorage
from core.models import generate_short_code


class RedisStorage(BaseStorage):
    def __init__(self):
        self.client = redis.from_url(settings.REDIS_URL)

    def save(self, long_url: str) -> str:
        short_code = generate_short_code()
        data = json.dumps({'long_url': long_url, 'click_count': 0})
        self.client.set(f'url:{short_code}', data)
        return short_code

    def get(self, short_code: str) -> str | None:
        raw = self.client.get(f'url:{short_code}')
        if not raw:
            return None
        data = json.loads(raw)
        data['click_count'] += 1
        self.client.set(f'url:{short_code}', json.dumps(data))
        return data['long_url']

    def delete(self, short_code: str) -> bool:
        result = self.client.delete(f'url:{short_code}')
        return result > 0

    def list_all(self) -> list:
        keys = self.client.keys('url:*')
        urls = []
        for key in keys:
            raw = self.client.get(key)
            if raw:
                data = json.loads(raw)
                data['short_code'] = key.decode().replace('url:', '')
                urls.append(data)
        return urls