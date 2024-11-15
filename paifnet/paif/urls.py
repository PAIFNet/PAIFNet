from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='login'),
    #path('recuperar-senha/', recuperar, name='recuperar'),
    path('verificar-login/', verificar_login, name="verificar_login"),
    path('logout/', logout, name="logout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('participantes/', participantes, name="participantes"),
    path('grupos/', grupos, name="grupos"),
    path('frequencia/', frequencia, name="frequencia"),
    path('lista-de-espera/', lista_de_espera, name="lista-de-espera"),
]
