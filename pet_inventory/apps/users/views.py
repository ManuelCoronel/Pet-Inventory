from django.shortcuts import redirect, render
from django import views
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Create your views here.


"""
Index View
"""
class index(views.View):
    """
    Get method for class View
    Return the index template
    """
    def get(self, request):
        return render(request, 'users/index.html')


"""
Iniciar Sesion View
"""
class iniciarSesion(views.View):
    """
    Get method for class IniciarSesion
    Return the inciarSesion template
    """
    def get(self, request):
        return render(request, 'users/iniciarSesion.html')

    """
    Post method for class IniciarSesion
    Athentication for user
    """
    def post(self, request):
        print(request.POST)
        username = request.POST['txtUsername']
        password = request.POST['txtPassword']
        user = authenticate(username=username, password=password)
        print(user)

        if user is None:
            return render(request, 'users/index.html')
        return redirect('/pets/dashboard')


"""
Registrar Usuario View
"""
class registrarUsuario(views.View):
    """
    Post method for class RegistrarUsuario
    Register a user
    """
    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        User.objects.create(username=username, email=email, password=password)
        return redirect('/pets/dashboard')
