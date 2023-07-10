from django.urls import path
from . import views

#URL Conf
urlpatterns = [
    path('index/', views.landing_page),
    path('about/', views.about),
]