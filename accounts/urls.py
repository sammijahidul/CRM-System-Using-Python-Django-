from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),


    path('', views.home, name="home"),
    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings, name="account"),
    path('products/', views.products, name="products"),
    path('customer/<str:new_value>/', views.customer, name="customer"),


    path('create_order/<str:new_value>', views.createOrder, name="create_order"),
    path('update_order/<str:new_value>', views.updateOrder, name="update_order"),
    path('delete_order/<str:new_value>', views.deleteOrder, name="delete_order"),

    path('reset_password/', auth_views.PasswordResetView.as_view())





]
