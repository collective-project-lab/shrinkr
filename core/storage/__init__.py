from django.conf import settings


def get_storage():
    if settings.USE_REDIS:
        from .redis import RedisStorage
        return RedisStorage()
    from .sqlite import SQLiteStorage
    return SQLiteStorage()