
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import mail_admins
from django.template.loader import render_to_string

from .models import Mistype


@receiver(post_save, sender=Mistype)
def email_notifier(sender, **kwargs):

    if not kwargs["created"]:
        return  # Send email only on new mistypes

    mistype = kwargs["instance"]
    context = {
        'url': mistype.url,
        'ip': mistype.ip,
        'mistype': mistype.full_text(),
        'comment': mistype.comment
    }

    mail_admins('Mistype', '',
                html_message=render_to_string('mistypes/mistype-email.html', context))
