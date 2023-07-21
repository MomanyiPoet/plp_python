from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#URL Conf
urlpatterns = [
    path('services/', views.services, name='services'),
    path('signup/', views.signup, name='signup'),
    path('', auth_views.LoginView.as_view(template_name = 'login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'logout.html'), name='logout'),
]