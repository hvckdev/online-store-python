from django.urls import path

from web_shop.shop import views

urlpatterns = [
    path('', views.ProductListView.as_view(), name='home'),
    path('orders', views.OrderListView.as_view(), name='orders'),
    path('products/<int:product_pk>/order', views.CreateOrderView.as_view(), name='create-order')
]
