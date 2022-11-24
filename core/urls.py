from django.urls import path, include
from django.views.i18n import JavaScriptCatalog
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static

from core.admin import auction_admin_site

urlpatterns = [
    path("i18n/", include("django.conf.urls.i18n")),
]

urlpatterns += i18n_patterns(path('jsi18n/', JavaScriptCatalog.as_view(), name='javascript-catalog')) # Ho tro da ngon ngu trong Javascript
urlpatterns += i18n_patterns(path("admin/", auction_admin_site.urls))
urlpatterns += i18n_patterns(path('', include('auction.urls', namespace='auction'), name='auction_url'))
urlpatterns += i18n_patterns(path('user/', include('authentication.urls', namespace='authentication'), name='authentication_url'))
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # User upload media file
