
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

class MistypesConfig(AppConfig):
    name = "mistypes"
    verbose_name = _("Mistypes")

    def ready(self):
        import mistypes.signals
