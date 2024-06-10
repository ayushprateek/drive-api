from django.core.cache import cache


def set(key, data, duration, *args, **kwargs):
    cache.set(key.format(*args, **kwargs), data, duration)


def get(key, *args, **kwargs):
    return cache.get(key.format(*args, **kwargs))


def delete(key, *args, **kwargs):
    return cache.delete(key.format(*args, **kwargs))
