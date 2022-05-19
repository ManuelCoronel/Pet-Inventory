from django.shortcuts import redirect, render
from django import views
from .models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
# Create your views here.


class index(views.View):
    """Index View"""

    def get(self, request):
        """Get method for class View, Return the index template"""
        return render(request, 'users/index.html')


class iniciarSesion(views.View):
    """Iniciar Sesion View"""

    def get(self, request):
        """Get method for class IniciarSesion, Return the inciarSesion template"""
        return render(request, 'users/iniciarSesion.html')

    def post(self, request):
        """Post method for class IniciarSesion, Athentication for user"""
        print(request.POST)
        username = request.POST['txtUsername']
        password = request.POST['txtPassword']
        user = authenticate(username=username, password=password)
        print(user)

        if user is None:
            return render(request, 'users/index.html')
        return redirect('/pets/dashboard')


class registrarUsuario(views.View):
    """Registrar Usuario View"""

    def post(self, request):
        """Post method for class RegistrarUsuario, Register a user"""
        username = request.POST['username']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        User.objects.create(username=username, email=email, password=password)
        return redirect('/pets/dashboard')
