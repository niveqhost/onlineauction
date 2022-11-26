from django.contrib import admin
from django.contrib.admin.apps import AdminConfig

from authentication.models import CustomUser
from authentication.admin import CustomUserTransAdmin

# Ke thua lop AdminConfig, tuy chinh lop AdminConfig
class AuctionAdminConfig(AdminConfig):
    default_site = 'core.admin.AuctionAdminArea'

# AuctionAdminSite
class AuctionAdminArea(admin.AdminSite):
    site_header: str = 'Auction Admin Area'

auction_admin_site = AuctionAdminArea(name='AuctionAdmin')

# Dang ki cac model o day
auction_admin_site.register(CustomUser, CustomUserTransAdmin)