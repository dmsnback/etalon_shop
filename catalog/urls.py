from django.urls import path

from catalog import views


app_name = 'catalog'


urlpatterns = [
    path('', views.index, name='index'),
    path('catalog/', views.catalog, name='allproducts'),
    path('product/<int:pk>', views.detail_product, name='detail')
]
