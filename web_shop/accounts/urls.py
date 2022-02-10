from django.urls import path

from web_shop.accounts import views

urlpatterns = [
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('accounts/profile/', views.profile, name='profile')
]