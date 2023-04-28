from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import MyLoginView

urlpatterns = [
    path('shoppingindex/', views.shoppingindex, name='shoppingindex'),
    path('shopping_detail/', views.shoppingdetail, name='shoppingdetail'),
    path('product_by_name/<str:value>/', views.product_by_name, name='product_by_name'),
    path('check_by_date/<path:date>/', views.check_by_date, name='check_by_date'),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', MyLoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('cart/',views.add_to_cart, name='cart'),

]