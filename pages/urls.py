from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('about/', views.AboutView, name='about'),
    path('contact/', views.ContactView, name='contact'),
    path('services/', views.ServicesView, name='services'),
    path('projects/', views.ProjectsView, name='projects'),
]
