from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#URL Conf
urlpatterns = [
    # USER URLS
    path('', views.landing_page, name='landing_page'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'user/logout.html'), name='logout'),
]