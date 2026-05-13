from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from ecom import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),         # Points to the HOME view
    path('store/', include('store.urls')),     # Points to the STORE app URLs
]
# ONLY add this if DEBUG is True and keep it at the VERY BOTTOM
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)