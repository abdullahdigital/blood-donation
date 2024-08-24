from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('about/', views.about, name='about'),
    path('volunteer/', views.volunteer_view, name='volunteer'),
    path('request-blood/', views.request_blood_view, name='request_blood'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('update-notification-status/<uuid:notification_id>/', views.update_notification_status, name='update_notification_status'),
    path('notification-count/', views.notification_count, name='notification_count'),
    path('request_blood_success/<uuid:request_id>/', views.request_blood_success, name='request_blood_success'),
]
