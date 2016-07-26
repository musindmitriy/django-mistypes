
from django.apps import AppConfig


class MistypesConfig(AppConfig):
    name = "mistypes"
    verbose_name = "Mistypes"

    def ready(self):
        pass