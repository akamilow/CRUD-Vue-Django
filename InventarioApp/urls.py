from django.urls import re_path as url
from InventarioApp import views

urlpatterns = [
    url(r'^producto$', views.producto_list),
    url(r'^producto/([0-9]+)$', views.producto_list),
]