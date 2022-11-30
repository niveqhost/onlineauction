from django.urls import reverse
from django.views import generic
from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required

from utils import constants
from auction import models, forms

# Create your views here.
# ------------------------------- Trang chu -------------------------------
class IndexView(generic.View):
    template_name = 'auction/index.html'

    def get(self, request):
        try:
            context = {}
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
            categories = models.CategoryModel.objects.all() 
            # Form san pham
            product_form = forms.ProductForm()
            context = {
                'categories' : categories,
                'form' : product_form
            }
            return render(request, self.template_name, context)
        except Exception as ex:
            print('ADD PRODUCT GET REQUEST ERROR: ', ex)

    def post(self, request, *args, **kwargs):
        try:
            categories = models.CategoryModel.objects.all()
            form = forms.ProductForm(request.POST)
            # TODO: Xu ly cho code nay
            if form.is_valid():
                product_name = form.cleaned_data.get('product_name')
                product = models.ProductModel(product_name=product_name)
                product.save()
                
                product_images = request.FILES.getlist('product_images')
                for image in product_images:
                    new_image = models.ProductImage(photo=image)
                    new_image.product_id = product.id
                    new_image.save()
                return
            context = { 
                'has_error': False, 
                'data': request.POST, 
                'categories' : categories 
            }
            self.validate_product(request, context)
            if context.get('has_error'):
                return render(request, self.template_name, context)
            messages.add_message(request, constants.MY_MESSAGE_LEVEL, _('Register product successfully.'), constants.MY_SUCCESS_TAG)
            context.pop('data')
            return render(request, self.template_name, context)
        except Exception as ex:
            print('ADD PRODUCT POST REQUEST ERROR: ', ex)

    #* Lam sach du lieu
    def validate_product(self, request, context) -> dict:
        try:
            product_name = request.POST.get('product_name')
            description = request.POST.get('description')
            category_id = request.POST.get('categories')
            if product_name == "" or description == "":
                messages.add_message(request, constants.MY_MESSAGE_LEVEL ,_("All fields are required."), constants.MY_ERROR_TAG)
                context['has_error'] = True
            if category_id is None:
                messages.add_message(request, constants.MY_MESSAGE_LEVEL ,_("Product category field is required."), constants.MY_ERROR_TAG)
                context['has_error'] = True
            return context
        except Exception as ex:
            print('VALIDATE PRODUCT ERROR: ', ex)
