
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from home import views

urlpatterns = [
    path('', include('home.urls')),
    path('about/', views.about , name='about'),
    path('references/', views.references , name='references'),
    path('contact/', views.contact , name='contact'),
    path('product/', include('product.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
