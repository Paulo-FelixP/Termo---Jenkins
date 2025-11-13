from django.urls import path
from . import views

urlpatterns = [
    path('', views.nivel1, name='index'),  # Página inicial agora abre o Nível 1
    path('nivel1/', views.nivel1, name='nivel1'),
    path('nivel2/', views.nivel2, name='nivel2'),
    path('nivel3/', views.nivel3, name='nivel3'),
]