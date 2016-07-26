
from django.db import models

from django.utils.html import format_html


class Mistype(models.Model):

    TYPE_CHOICES = (
        ('O', 'opened'),
        ('S', 'spam'),
        ('P', 'in progress'),
        ('C', 'closed'),
        ('N', 'not a mistake')
    )

    type = models.CharField(verbose_name="Type", max_length=1, choices=TYPE_CHOICES)
    ip = models.GenericIPAddressField(verbose_name="IP")
    url = models.URLField(verbose_name="Mistype URL", max_length=300)

    before = models.CharField(verbose_name="Before mistype", max_length=50)
    mistype = models.CharField(verbose_name="Mistype", max_length=100)
    after = models.CharField(verbose_name="After mistype", max_length=50)

    comment = models.TextField(verbose_name="Comment", max_length=200, blank=True)

    date = models.DateTimeField(verbose_name="Date", auto_now=True)

    def full_text(self):
        return format_html('{}<span style=color:black;text-decoration:underline>{}</span>{}',
                           self.before, self.mistype, self.after)
    full_text.allow_tags = True

