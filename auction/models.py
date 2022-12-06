from django.db import models
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

# Ung dung ben thu ba
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from authentication.models import CustomUser

# Create your models here.

# Danh muc san pham
class CategoryModel(models.Model):
    # Ma danh muc - Tu tao boi framework
    # Ten danh muc
    category_name = models.CharField(max_length=150, blank=False)
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self) -> str:
        return self.category_name

# San pham
class ProductModel(models.Model):
    # Ma san pham - Tu tao boi framework
    # Ten san pham
    product_name = models.CharField(max_length=255, blank=False)
    # Gia thap nhat cua san pham
    minimum_price = models.IntegerField(blank=True, validators=[MinValueValidator(1)],default=1)
    # Khoa ngoai: Ma danh muc - 1 danh muc co nhieu san pham
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    # Khoa ngoai: Nguoi ban - 1 nguoi co the ban nhieu san pham
    # seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Khoa ngoai: Nguoi dau gia - 1 san pham duoc nhieu nguoi dau gia
    # bidder = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Anh dai dien san pham
    thumbnail = models.ImageField(null=True, blank=True, upload_to='product_images/thumbnail')
    # Mo ta chi tiet
    description = RichTextField(blank=True, null=True)
    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self) -> str:
        return self.product_name

# Anh san pham
class ProductImage(models.Model):
    # Ma hinh anh - Tu tao boi framework   
    product_images = models.ImageField(null=True, blank=True, upload_to='product_images')
    # Khoa ngoai: Ma san pham - 1 san pham co nhieu anh
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)
    class Meta:
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')

    def __str__(self) -> str:
        return str(self.id)
    
# Phien dau gia
class AuctionLot(models.Model):
    class Meta:
        verbose_name = _('Lot')
        verbose_name_plural = _('Lots')

    def __str__(self) -> str:
        return str(self.id)

# Lich su dau gia
class AuctionHistoryModel(models.Model):
    class Meta:
        verbose_name = _('History')
        verbose_name_plural = _('Histories')

    def __str__(self) -> str:
        return str(self.id)

# Danh sach ua thich
class WishlistModel(models.Model):
    class Meta:
        verbose_name = _('Wishlist')
        verbose_name_plural = _('Wishlists')

    def __str__(self) -> str:
        return str(self.id)

# Phan hoi cua khach hang
class FeedbackModel(models.Model):
    class Meta:
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')

    def __str__(self) -> str:
        return str(self.id)