from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginView, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logoutView, name='logout'),

    # Password reset URLs
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='cms/password_reset.html',
        email_template_name='cms/password_reset_email.html',
        subject_template_name='cms/password_reset_subject.txt',
        success_url='/cms/password-reset/done/'
    ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='cms/password_reset_done.html'
    ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='cms/password_reset_confirm.html',
        success_url='/cms/reset/done/'
    ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='cms/password_reset_complete.html'
    ), name='password_reset_complete'),

]
