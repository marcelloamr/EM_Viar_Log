from django.contrib import admin
from django.urls import path, include  # Inclui o include

urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o painel admin
    path('', include('website.urls')),  # Inclui as rotas do app website
]
