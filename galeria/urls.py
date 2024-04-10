from django.urls import path
from galeria.views import buscar, index, imagem, filtrar

urlpatterns = [
    path('', index, name='index'),
    path('imagem/<int:foto_id>', imagem, name='imagem'),
    path('buscar/', buscar, name='buscar'),
    path('filtrar/<filtro>', filtrar, name='filtrar')
]
