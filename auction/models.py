from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _

# Ung dung ben thu ba
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from authentication.models import CustomUser
from utils import constants

# Create your models here.

# Danh muc san pham
class CategoryModel(models.Model):
    # Ma danh muc - Tu tao boi framework
    # Ten danh muc
    category_name = models.CharField(max_length=150, blank=False)
    # Anh danh muc
    category_image = models.ImageField(null=True, blank=True, upload_to='category_images')
    # Slug
    category_slug = models.SlugField(max_length = 255, null=True, blank=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.category_slug:
            self.category_slug = slugify(self.category_name + "-")
        return super().save(*args, **kwargs)

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
    # Khoa ngoai: Ma danh muc - 1 danh muc co nhieu san pham
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True)
    # Khoa ngoai: Nguoi ban - 1 nguoi co the ban nhieu san pham
    seller = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    # Khoa ngoai: Nguoi dau gia - 1 san pham duoc nhieu nguoi dau gia
    # bidder = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Anh dai dien san pham
    product_thumbnail = models.ImageField(null=True, blank=True, upload_to='product_images/thumbnail')
    # Mo ta chi tiet
    description = RichTextField(blank=True, null=True)
    # Slug
    product_slug = models.SlugField(max_length=255, null=True, blank=True, unique=True)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')

    def __str__(self) -> str:
        return self.product_name

    def save(self, *args, **kwargs):
        if not self.product_slug:
            self.product_slug = slugify(self.product_name + "-")
        return super().save(*args, **kwargs)

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
    # Thoi diem bat dau
    start_time = models.DateTimeField(default=timezone.now, null=True)
    # Thoi diem ket thuc
    end_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(hours=constants.TIME_DURATION))
    # Da ket thuc hay chua
    is_ended = models.BooleanField(default=False)
    # Duoc phe duyet hay khong
    is_active = models.BooleanField(default=False)
    # San pham
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, null=True)
    # Gia thap nhat cua phien dau gia
    minimum_price = models.IntegerField(blank=True, validators=[MinValueValidator(0)], default=0.0)
    # Buoc nhay
    bid_increament = models.IntegerField(default=0.0, blank=True)
    # Gia hien tai
    current_price = models.IntegerField(default=0.0)

    class Meta:
        verbose_name = _('Lot')
        verbose_name_plural = _('Lots')

    def __str__(self) -> str:
        return str(self.id)

# Lich su dau gia
class AuctionHistory(models.Model):
    auction = models.ForeignKey(AuctionLot, on_delete=models.CASCADE,related_name='auction', null=True) 
    bidder = models.ForeignKey(CustomUser, related_name='bidder',on_delete=models.CASCADE, null=True)
    date_bidded = models.DateTimeField(auto_now_add=True, help_text='when the bid was made')
    price = models.IntegerField(default=0.0)

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