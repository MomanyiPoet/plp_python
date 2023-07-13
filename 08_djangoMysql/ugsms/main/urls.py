from django.urls import path
from . import views

#URL Conf
urlpatterns = [
    path('', views.landing_page, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]