from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='FAQ'),


]
