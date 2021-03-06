
import threading

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_admins
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _

from .models import Mistype


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

        mail_admins(_('New mistype'), '',
                    html_message=render_to_string('mistypes/mistype-email.html', context))


@receiver(post_save, sender=Mistype)
def email_notifier(sender, **kwargs):

    if not kwargs["created"]:
        return  # Send email only on new mistypes

    mistype = kwargs["instance"]
    MailThread(mistype).start()

