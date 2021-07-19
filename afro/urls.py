from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


app_name = 'afro'
urlpatterns = [
    path('', views.index, name='home'),
    path('about-us/', views.about, name='aboutus'),
    path('more-info/<str:pk>/', views.info, name='more-info'),

    path('register/', views.register, name='register'),
    path('login/', views.login1, name='login'),
    path('logout/', views.logoutUser, name='logout'),

]    