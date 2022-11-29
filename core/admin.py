from django.contrib import admin
from django.contrib.admin.apps import AdminConfig

from authentication.models import CustomUser, ProfileModel
from authentication.admin import CustomUserTransAdmin, ProfileModelTransAdmin

from auction.models import CategoryModel
from auction.admin import CategoryTransAdmin

# Ke thua lop AdminConfig, tuy chinh lop AdminConfig
class AuctionAdminConfig(AdminConfig):
    default_site = 'core.admin.AuctionAdminArea'

# AuctionAdminSite
class AuctionAdminArea(admin.AdminSite):
    site_header: str = 'Auction Admin Area'

auction_admin_site = AuctionAdminArea(name='AuctionAdmin')

# Dang ki cac model o day
auction_admin_site.register(CustomUser, CustomUserTransAdmin)
auction_admin_site.register(ProfileModel, ProfileModelTransAdmin)
auction_admin_site.register(CategoryModel, CategoryTransAdmin)