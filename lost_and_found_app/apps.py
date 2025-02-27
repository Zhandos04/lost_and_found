from django.apps import AppConfig
from django.db.utils import OperationalError

class LostAndFoundAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lost_and_found_app'

    def ready(self):
        from .models import Category
        default_categories = ['Electronics', 'Clothing', 'Documents', 'Accessories', 'Others']
        try:
            for category in default_categories:
                Category.objects.get_or_create(name=category)
        except OperationalError:
            pass
