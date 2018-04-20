from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('shops_nearby/', include('shops_nearby.urls')),
    path('', RedirectView.as_view(url='/shops_nearby/')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('shops_nearby.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
