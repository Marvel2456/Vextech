from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.loginView, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logoutView, name='logout'),

    # Navigation URLs
    path('view_contact', views.viewContact, name='view_contact'),
    path('view_projects', views.viewProjects, name='view_projects'),
    path('load_project_modal', views.loadProjectModal, name='load_project_modal'),
    path('edit_project/<uuid:pk>/', views.editProject, name='edit_project'),
    path('load_edit_project_modal/<uuid:pk>/', views.loadEditProjectModal, name='load_edit_project_modal'),
    path('delete_project/<uuid:pk>/', views.deleteProject, name='delete_project'),
    path('load_delete_project_modal/<uuid:pk>/', views.loadDeleteProjectModal, name='load_delete_project_modal'),
    path('create_project', views.createProject, name='create_project'),
    path('view_services', views.viewServices, name='view_services'),
    path('view_newsletter', views.NewsletterView, name='view_newsletter'),
    path('view_visits', views.viewVisits, name='view_visits'),

    # path('view_project/<slug:slug>/', views.viewProject, name='view_project'),
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
