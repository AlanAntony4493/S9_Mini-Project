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
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('about', views.about, name='about'),



    path('report_admin/', views.report_admin, name='report_admin'),
    path('generate-pdf/<str:year>/', views.generate_pdf, name='generate_pdf'),
    path('generate-archived-pdf/<int:year>/', views.generate_archived_pdf, name='generate_archived_pdf'),

    # path('login/', LoginView.as_view(template_name="login.html",next_page="index"), name='login'),
    path('media-manager-login/', views.media_manager_login_view, name='media_manager_login'),
    path('accounted-user-login/', views.accounted_user_login_view, name='accounted_user_login'),
    path('logout', views.logout, name='logout'),
    path('event',views.event, name='event'),
    path('archive_event/<int:event_id>/', views.archive_event, name='archive_event'),
    path('del_event/<int:event_id>/', views.del_event, name='del_event'),
    path('unarchive_event/<int:event_id>/', views.unarchive_event, name='unarchive_event'),
    path('by_law',views.by_law, name="by_law"),
    path('register',views.register, name="register"),
    path('index_admin',views.index_admin, name="index_admin"),
    path('user_admin',views.user_admin, name="user_admin"),
    path('index_home',views.index_home, name="index_home"),
    path('blood_admin',views.blood_admin, name="blood_admin"),
    path('parish_admin',views.parish_admin, name="parish_admin"),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    # path('delete-donor/<int:pk>/', views.delete_donor, name='delete_donor'),
    path('soft-delete-donor/<int:donor_id>/', views.soft_delete_donor, name='soft_delete_donor'),
    path('blood_user/<str:blood_group>/', views.filtered_donor_list, name='filtered_donor_list'),
    path('approve_user/<int:user_id>/', views.approve_user, name='approve_user'),
    path('get_archived_reports/', views.get_archived_reports, name='get_archived_reports'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    path('retrieve_deleted_prayer_group/<int:entity_id>/', views.retrieve_deleted_entity, {'entity_type': 'prayer_group'}, name='retrieve_deleted_prayer_group'),
    path('retrieve_deleted_parish_member/<int:entity_id>/', views.retrieve_deleted_entity, {'entity_type': 'parish_member'}, name='retrieve_deleted_parish_member'),
    path('update_parish/<int:member_id>/', views.update_parish, name='update_parish'),
    path('profile/', views.profile, name='profile'),
    path('career_forum/', views.career_forum, name='career_forum'),
    path('post_question/', views.post_question, name='post_question'),
    path('post_answer/', views.post_answer, name='post_answer'),
    path('soft_delete_answer/<int:answer_id>/', views.soft_delete_answer, name='soft_delete_answer'),
    path('soft_delete_question/<int:question_id>/', views.soft_delete_question, name='soft_delete_question'),
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),
    path('edit_comment/<int:answer_id>/', views.edit_comment, name='edit_comment'),
    path('report/comment/<int:answer_id>/', views.report_comment, name='report_comment'),
    path('reported_comments/', views.reported_comments, name='reported_comments'),
    path('donation_form/', views.donation_form, name='donation_form'),
    path('paymentform/', views.paymentform, name='paymentform'),
    path('soft_delete_reported_answer/<int:answer_id>/', views.soft_delete_reported_answer, name='soft_delete_reported_answer'),
    path('edit_question/<int:question_id>/', views.edit_question, name='edit_question'),
    path('add_resource_person/', views.add_resource_person, name='add_resource_person'),
    # quiz
    
    path('quiz', views.quiz, name='quiz'),

    # gallery
    path('inner_page/<int:album_id>/', views.inner_page, name='inner_page'),
    path('gallery',views.gallery, name="gallery"),

    # profile
    path('view_profile/', views.view_profile, name='view_profile'),


    #admin approval for id card
    path('virtual_id_approval/', views.virtual_id_approval, name='virtual_id_approval'),
    path('virtual_id_approval/approve/<int:id>/',views.approve_id, name='approve_id'),
    path('virtual_id_approval/reject/<int:id>/', views.reject_id, name='reject_id'),
    # path('virtual_id_approval/reject/<int:id>/', views.reject_id, name='reject_id'),

    # Accountant
    path('accounts/', views.accounts, name='accounts'),
    path('add_transaction/', views.add_transaction, name='add_transaction'),

    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)