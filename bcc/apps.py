from django.apps import AppConfig


class BccConfig(AppConfig):
    name = 'bcc'

    def ready(self):
        import bcc.signals
