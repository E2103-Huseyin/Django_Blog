from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'myblog'

    def ready(self):
        import myblog.signals