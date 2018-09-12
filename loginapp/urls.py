from django.conf.urls import include, url
from .views import home_page,login_page,register_page, index_page,logout_page
from django.contrib import admin
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',index_page, name='index'),
    url(r'^login/$', login_page, name='login'),
    url(r'^home/$', home_page, name='home'),
    url(r'^register/$', register_page, name='register'),
    url(r'^logout/$',logout_page, name='logout'),
]