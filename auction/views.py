from django.shortcuts import render
from django.views import generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from auction.models import CategoryModel

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
            categories = CategoryModel.objects.all()
            context = {
                'categories' : categories
            }
            return render(request, self.template_name, context)
        except Exception as ex:
            print('ADD PRODUCT GET REQUEST ERROR: ', ex)

    def post(self, request, *args, **kwargs):
        try:
            pass
        except Exception as ex:
            print('ADD PRODUCT POST REQUEST ERROR: ', ex)
