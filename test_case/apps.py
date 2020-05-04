from django.apps import AppConfig


class TestCaseConfig(AppConfig):
    name = 'test_case'

    def ready(self):
        import test_case.signals
