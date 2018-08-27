"""django_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path, re_path
from accounts.views import index, user_login, user_logout
from accounts import urls as accounts_urls
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', index, name="index"),
    path('accounts/', include(accounts_urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^login/$',user_login, name="login" ),
    url(r'^logout/$', user_logout, name="logout"),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(), name="passwordreset"),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view()),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    auth_views.PasswordResetConfirmView.as_view()),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view()),
]

    
