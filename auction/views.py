from django.shortcuts import render
from django.views import generic

# Create your views here.
# view cho trang chu
class IndexView(generic.View):
    template_name = 'auction/index.html'

    def get(self, request):
        try:
            context = {}
            return render(request, self.template_name, context)
        except Exception as ex:
            print('INDEX PAGE GET REQUEST ERROR: ', ex)
