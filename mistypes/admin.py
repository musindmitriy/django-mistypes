
from django.contrib import admin

from .models import Mistype


class MistypeAdmin(admin.ModelAdmin):
    list_display = ('full_text', 'type', 'ip', 'url', 'comment')
    list_filter = ('type', )
    list_editable = ('type', )

admin.site.register(Mistype, MistypeAdmin)
