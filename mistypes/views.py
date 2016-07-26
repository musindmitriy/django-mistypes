
import threading

from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.template.loader import render_to_string

from django.conf import settings

from .forms import MistypeForm
from .utils import get_client_ip, is_referer_url, is_url_allowed


class MailThread(threading.Thread):
    def __init__(self, mistype, **kwargs):
        self.mistype = mistype
        super(MailThread, self).__init__(**kwargs)

    def run(self):
        mistype = self.mistype
        context = {
            'url': mistype.url,
            'ip': mistype.ip,
            'mistype': mistype.full_text(),
            'comment': mistype.comment
        }

        send_mail('Mistype', '', settings.DEFAULT_FROM_EMAIL, [settings.DEFAULT_TO_EMAIL],
                  html_message=render_to_string('mistypes/mistype-email.html', context))


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

                MailThread(mistype).start()
                mistype.save()

                return HttpResponse("")

    raise PermissionDenied


if settings.MISTYPES_CSRF_EXEMPT:
    submit = csrf_exempt(submit)


