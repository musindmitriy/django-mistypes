
from urllib.parse import urlparse

from django.conf import settings


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

    if x_forwarded_for:
        return x_forwarded_for.partition(',')[0]

    return request.META.get('REMOTE_ADDR')


def is_referer_url(request, url):
    referer = request.META.get('HTTP_REFERER')
    return referer == url


def is_url_allowed(url):
    return settings.DEBUG or urlparse(url).hostname in settings.ALLOWED_HOSTS
