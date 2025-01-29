"""
URL configuration for djangoGraduateWork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from djangoGraduateApp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('main_dishes_page/', main_dishes_page),
    path('registration_page/', registration_page),
    path('login_page/', login_page),
    path('user_data_page/', user_data_page),
    path('dolma_info/', dolma_info),
    path('falaf_info/', falaf_info),
    path('meat_bites_info/', meat_bites_info),
    path('plov_info/', plov_info),
    path('potato_info/', potato_info),
    path('ragu_info/', ragu_info),
    path('pizza_page/', pizza_page),
    path('marg_info/', marg_info),
    path('mush_info/', mush_info),
    path('pep_info/', pep_info),
    path('sea_info/', sea_info),
    path('drinks_page/', drinks_page),
    path('cof_info/', cof_info),
    path('ju_info/', ju_info),
    path('milksh_info/', milksh_info),
    path('zero_info/', zero_info),
    path('desserts_info/', desserts_info),
    path('bun_info/', bun_info),
    path('cookie_info/', cookie_info),
    path('ice_info/', ice_info),
    path('pie_info/', pie_info),
    path('client_orders_page/', client_orders_page),
    path('redirect/', redirect),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)