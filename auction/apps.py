from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

class AuctionConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'auction'
    verbose_name: str = _("Auction")
