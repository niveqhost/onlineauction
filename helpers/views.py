from django.shortcuts import render

#* Xu li loi khong tim thay trang 404
def handle_not_found(request, exception):
    return render(request, '_partials/404-not-found.html')

#* Xu li loi server 500
def handle_server_error(request):
    return render(request, '_partials/500-server-error.html')