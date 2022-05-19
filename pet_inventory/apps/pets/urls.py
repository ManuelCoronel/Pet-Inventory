from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard.as_view(), name='dashboard'),
    path('eliminar/<id>', views.eliminarPets.as_view(), name='dashboard'),
    path('editarPet/<id>', views.editarPets.as_view(), name='dashboard'),
    path('editarPet/', views.editarPets.as_view(), name='dashboard'),
]
