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
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout, name='logout'),
    path('event',views.event, name='event'),
    path('archive_event/<int:event_id>/', views.archive_event, name='archive_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('unarchive_event/<int:event_id>/', views.unarchive_event, name='unarchive_event'),
    path('by_law',views.by_law, name="by_law"),
    path('register',views.register, name="register"),
    path('index_admin',views.index_admin, name="index_admin"),
    path('user_admin',views.user_admin, name="user_admin"),
    path('index_home',views.index_home, name="index_home"),
    path('blood_admin',views.blood_admin, name="blood_admin"),
    path('parish_admin',views.parish_admin, name="parish_admin"),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('delete-donor/<int:pk>/', views.delete_donor, name='delete_donor'),
    path('blood_user/<str:blood_group>/', views.filtered_donor_list, name='filtered_donor_list'),
    path('approve_user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('report_admin', views.report_admin, name='report_admin'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('gallery',views.gallery, name="gallery"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)