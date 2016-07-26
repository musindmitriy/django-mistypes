
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.conf import settings

from .forms import MistypeForm
from .utils import get_client_ip, is_referer_url, is_url_allowed


def submit(request):

    if not request.is_ajax():
        raise PermissionDenied

    if request.method == 'POST':
        form = MistypeForm(request.POST)

        if form.is_valid():
            mistype = form.save(commit=False)
            if is_referer_url(request, mistype.url) and is_url_allowed(mistype.url):
                mistype.type = 'O'
                mistype.ip = get_client_ip(request)
                mistype.save()

                return HttpResponse("")

    raise PermissionDenied


if settings.MISTYPES_CSRF_EXEMPT:
    submit = csrf_exempt(submit)


