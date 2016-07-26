
from django.db import models
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _


class Mistype(models.Model):

    class Meta:
        verbose_name = _('Mistype')
        verbose_name_plural = _('Mistypes')

    TYPE_CHOICES = (
        ('O', _('opened')),
        ('S', _('spam')),
        ('P', _('in progress')),
        ('C', _('closed')),
        ('N', _('not a mistake'))
    )

    type = models.CharField(verbose_name=_("Type"), max_length=1, choices=TYPE_CHOICES)
    ip = models.GenericIPAddressField(verbose_name=_("IP"))
    url = models.URLField(verbose_name=_("Mistype URL"), max_length=300)

    before = models.CharField(verbose_name=_("Before mistype"), max_length=50)
    mistype = models.CharField(verbose_name=_("Mistype text"), max_length=100)
    after = models.CharField(verbose_name=_("After mistype"), max_length=50)

    comment = models.TextField(verbose_name=_("Comment"), max_length=200, blank=True)

    date = models.DateTimeField(verbose_name=_("Date"), auto_now=True)

    def full_text(self):
        return format_html('{}<span style=color:black;text-decoration:underline>{}</span>{}',
                           self.before, self.mistype, self.after)
    full_text.allow_tags = True

