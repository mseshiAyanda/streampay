from django.urls import path
from django.conf.urls import url
from . import views
from .views import Register, Login
from django.contrib.auth import views as auth_views


app_name = 'afro'
urlpatterns = [
    path('', views.home, name='home'),
    url(r'^login/$', views.signin, name='login'),
    url(r'^check-mail-ajax/$', views.check_mail_ajax, name='check_mail_ajax'),
    path('about-us/', views.about, name='aboutus'),
    url(r'^register/$', Register.as_view(), name='register'),
    url(r'login-req', Login.as_view(), name='login_ajax'),
    path('more-info/<str:pk>/', views.info, name='more-info'),

    url(r'^subscription/', views.subscription, name='subscription'),
    url(r'^subscribe/', views.subscribe, name='subscribe'),
    url(r'^subscribed/', views.subscribed, name='subscribed'),
    url(r'^sub/', views.end_sub, name='sub'),

    url(r'^payment/$', views.call_back_url, name='payment'),


]    