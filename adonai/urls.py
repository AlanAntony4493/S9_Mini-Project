"""
URL configuration for adonai project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout, name='logout'),
    path('event',views.event, name='event'),
    path('by_law',views.by_law, name="by_law"),
    path('register',views.register, name="register"),
    path('index_admin',views.index_admin, name="index_admin"),
    path('user_admin',views.user_admin, name="user_admin"),
    path('index_home',views.index_home, name="index_home"),
    path('blood_admin',views.blood_admin, name="blood_admin"),
    path('blood_user',views.blood_user, name="blood_user"),
    path('parish_admin',views.parish_admin, name="parish_admin"),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('delete-donor/<int:pk>/', views.delete_donor, name='delete_donor'),
    path('blood_user/<str:blood_group>/', views.filtered_donor_list, name='filtered_donor_list'),
    path('approve_user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('parish_user', views.parish_user, name='parish_user'),
    path('event_user', views.event_user, name='event_user'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)