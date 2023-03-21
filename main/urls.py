from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = "main"

urlpatterns = [
    path('',views.index),
    path('index/', views.index),
    path('contact/', views.contact, name="contact"),
    path('demo/', views.demo, name="demo"),
    path('about/', views.about, name="about"),
    path('service/', views.service, name="service"),
    path('profile/', views.profile, name="profile"),
    path('profile/userinfo/', views.userinfo, name="userinfo"),
    # path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('login/', views.login, name='login'),
    path('password/', views.password, name='password'),
    path('register/', views.register, name='register'),
]