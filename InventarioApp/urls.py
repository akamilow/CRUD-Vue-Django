from django.urls import re_path as url
from InventarioApp import views

urlpatterns = [
    url(r'^producto$', views.producto_list),
    url(r'^producto/([0-9]+)$', views.producto_list),
    url(r'^cocina$', views.cocina_list),
    url(r'^cocina/([0-9]+)$', views.cocina_list),
    url(r'^limpieza$', views.limpieza_list),
    url(r'^limpieza/([0-9]+)$', views.limpieza_list),
    url(r'^proveedor$', views.proveedor_list),
    url(r'^proveedor/([0-9]+)$', views.proveedor_list)
]