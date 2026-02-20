
from django.contrib import admin
from django.urls import path
from galeria.views import index  # Importa a função que você criou

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),  # O caminho vazio '' significa a página inicial (localhost:8000)
]