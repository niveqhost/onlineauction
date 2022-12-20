import json
from django.views import generic
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from auction.forms import *
from utils import constants
from auction.models import *

# Create your views here.
# ------------------------------- Trang chu -------------------------------
class IndexView(generic.View):
    template_name = 'auction/index.html'

    def get(self, request, *args, **kwargs):
        try:
            # Lay ra tat ca danh muc
            categories_count = CategoryModel.objects.count()
            half_category_list = int(categories_count/2)
            # Lay ra N/2 danh muc dau tien
            categories_list_one = CategoryModel.objects.all()[:half_category_list]
            # Lay ra N - N/2 danh muc con lai
            categories_list_two = CategoryModel.objects.all()[half_category_list:]
            # Lay ra tat ca phien dau gia
            auctions = AuctionLot.objects.filter(is_active=True)
            products = set()
            for auction in auctions:
                product = ProductModel.objects.get(pk=auction.product_id)
                products.add(product)
            context = {
                'categories_list_one' : categories_list_one,
                'categories_list_two' : categories_list_two,
                # 'date': '2022/12/8',
                'auctions' : auctions,
                'products' : products
            }
            return render(request, self.template_name, context)
        except Exception as ex:
            print('INDEX PAGE GET REQUEST ERROR: ', ex)

#  ------------------ Nguoi ban dang ki san pham de dau gia ------------------
class AddProduct(generic.View):
    template_name = 'auction/add_product.html'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        try:
            #* Xoa tat ca tin nhan thong bao sau khi dang nhap
            storage = messages.get_messages(request)
            for _ in storage: 
                pass
            if len(storage._loaded_messages) == 1: 
                del storage._loaded_messages[0]
            # Model danh muc san pham
            categories = CategoryModel.objects.all() 
            # Form san pham
            product_form = ProductForm()
            image_form = ImageForm()
            context = {
                'categories' : categories,
                'product_form' : product_form,
                'image_form' : image_form
            }
            return render(request, self.template_name, context)
        except Exception as ex:
            print('ADD PRODUCT GET REQUEST ERROR: ', ex)

    def post(self, request, *args, **kwargs):
        try:
            categories = CategoryModel.objects.all()
            product_form = ProductForm(data=request.POST)
            product_images = request.FILES.getlist('product_images')
            #* Truong hop thong tin nguoi dung dien vao la hop le
            if product_form.is_valid():
                product_name = product_form.cleaned_data.get('product_name')
                description = product_form.cleaned_data.get('description')
                product = product_form.save(commit=False)
                product.product_name = product_name
                product.description = description
                product.save()
                for product_image in product_images:
                    ProductImage.objects.create(product_images=product_image,product=product)
                #* Hien thi thong bao cho nguoi dung
                messages.add_message(request, constants.MY_MESSAGE_LEVEL, _('Register product successfully.'), constants.MY_SUCCESS_TAG)
                return redirect('auction:index')
            #* Truong hop thong tin khong hop le
            context = { 
                'categories' : categories,
                'product_form' : product_form,
            }
            #* Hien thi loi
            print("PRODUCT FORM HAS ERRORS: ", product_form.errors)
            return render(request, self.template_name, context)
        except Exception as ex:
            print('ADD PRODUCT POST REQUEST ERROR: ', ex)

#  ------------------ Nguoi mua co the xem thong tin tat ca san pham ------------------
class ProductView(generic.View):
    template_name = 'auction/product.html'

    def get(self, request, *args, **kwargs):
        try:
            context = {
                'product_list': ProductModel.objects.order_by('id'),
            }
            return render(request, self.template_name, context)
        except Exception as ex:
            print('VIEW PRODUCT GET REQUEST ERROR: ', ex)

    def post(self, request, *args, **kwargs):
        try:
            pass
        except Exception as ex:
            print('VIEW PRODUCT POST REQUEST ERROR: ', ex)

# ---------------- Nguoi mua co the xem chi tiet san pham ---------------- 
# --------------------- va co the dau gia san pham -----------------------
class ProductDetail(generic.View):
    template_name = 'auction/product_detail.html'

    def get(self, request, product_id, product_slug, *args, **kwargs):
        try:
            # if timezone.now() < auction.end_time:
            #* Lay ra id cua san pham
            product = get_object_or_404(ProductModel, id=product_id,product_slug=product_slug)
            auction = get_object_or_404(AuctionLot, product_id=product_id)
            room = False
            product_images = ProductImage.objects.filter(product_id=product.pk)
            #* Xac thuc nguoi dung
            if request.user.is_authenticated:
                room= request.user
            context = {
                'room_name_json' : mark_safe(json.dumps(product_id)),
                'username' : mark_safe(json.dumps(request.user.username)),
                'room' : room,
                # ===============
                'product' : product,
                'product_images' : product_images,
                'auction' : auction, 
            }
            return render(request, self.template_name, context)
        except Exception as ex:
            print('PRODUCT DETAIL GET REQUEST ERROR: ', ex)

    def post(self, request, *args, **kwargs):
        try:
            pass
        except Exception as ex:
            print('PRODUCT DETAIL POST REQUEST ERROR: ', ex)

#  ------------------ Xem chi tiet danh muc san pham ------------------
class CategoryDetail(generic.View):
    template_name = 'auction/category_detail.html'

    def get(self, request, category_slug, *args, **kwargs):
        try:
            category = CategoryModel.objects.get(category_slug=category_slug)
            context = {
                'product_list': ProductModel.objects.filter(category_id=category.pk)
            }
            return render(request, self.template_name, context)
        except Exception as ex:
            print('CATEGORY DETAIL GET REQUEST ERROR: ', ex)

    def post(self, request, *args, **kwargs):
        try:
            pass
        except Exception as ex:
            print('CATEGORY DETAIL POST REQUEST ERROR: ', ex)