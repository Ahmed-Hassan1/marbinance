from django.apps import AppConfig


class SortingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sorting'

    def ready(self):
        from jobs import updater
        updater.start()