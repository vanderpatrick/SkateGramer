from django.apps import AppConfig


class SkateappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'skateapp'

    def ready(self):
        import skateapp.signals