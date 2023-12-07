from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', include('django.contrib.auth.urls'), name='login'),
    path('', Login, name='login'),
    path('product_list/', List_Products, name='list'),
    path('create_product/', Create_product, name='create'),
    path('edit_product/<int:id>', Edit_Product, name='edit_product'),
    path('delete_product/<int:id>', Delete_Product, name='delete_product')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)