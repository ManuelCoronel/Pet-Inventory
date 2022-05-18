from django.urls import path
from . import views
urlpatterns = [
  path('', views.index.as_view(), name='index'),
  path('iniciarSesion/', views.iniciarSesion.as_view(), name='iniciarSesion'),
  path('registrarUsuario/', views.registrarUsuario.as_view(), name='iniciarSesion'),
]
