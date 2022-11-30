from django.contrib import admin
from django.contrib.admin.apps import AdminConfig

from authentication.models import *
from authentication.admin import *
from auction.models import *
from auction.admin import * 

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
auction_admin_site.register(ProductModel, ProductAdmin)