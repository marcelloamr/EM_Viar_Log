from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.services, name='services'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cities/', views.cities_view, name='cities'),
    path('cubagem/', views.cubagem, name='cubagem'),
]
