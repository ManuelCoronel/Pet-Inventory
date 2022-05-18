from django.shortcuts import render, redirect
from django import views
from .models import Pet
# Create your views here.


"""
Dashboard View
"""
class dashboard(views.View):
    """
    Get method for class Dashboard
    Return the dashboard template
    """
    def get(self, request):
        pets = Pet.objects.all()
        return render(request, 'pets/dashboard.html', {'pets': pets})

    """
    Post method for class Dashboard
    Register a pet and return the dashboard template
    """
    def post(self, request):
        name = request.POST['name']
        species = request.POST['species']
        age = request.POST['age']
        quantity = request.POST['quantity']
        print(request)
        Pet.objects.create(name=name, species=species, age=age, quantity=quantity)
        
        return redirect('/pets/dashboard')


"""
Eliminar Pets View
"""
class eliminarPets(views.View):
    """
    Get method for class EliminarPet
    Delete a Pet
    """
    def get(self, request, id):
        pet = Pet.objects.get(id=id)
        pet.delete()
        return redirect('/pets/dashboard')


"""
Editar Pets View
"""
class editarPets(views.View):
    """
    Get method for class EditarPet
    Return editarPet template
    """
    def get(self, request, id):
        pet = Pet.objects.get(id=id)
        return render(request, 'pets/editarPet.html', {'pet': pet})

    """
    Post method for class Editar
    Edit a pet and return the dashboard template    
    """
    def post(self, request):
        pet = Pet.objects.filter(id=request.POST['id']).first()
        print(pet)
        pet.name = request.POST['name']
        pet.species = request.POST['species']
        pet.age = request.POST['age']
        pet.quantity = request.POST['quantity']
        pet.save()
        return redirect('/pets/dashboard')
