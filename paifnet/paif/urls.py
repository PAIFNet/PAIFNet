from django.urls import path
from .views import *

urlpatterns = [
    path('', login, name='login'),
    path('recuperar-senha/', recuperar, name='recuperar'),
    path('verificar-login/', verificar_login, name="verificar_login"),
    path('dashboard/', dashboard, name="dashboard")
]
