from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import IngredientForm, ApplianceForm
from django.contrib import messages
# Create your views here.
def create_appliance(request):
    if request.method == 'POST':
        form = ApplianceForm(request.POST)
        if form.is_valid():
            appliance = form.save()
            return redirect('appliance-detail', pk=appliance.id)
    else:
        form = ApplianceForm()
    return render(request, 'cooking/appliance_form.html', {'form': form})

def update_appliance(request, appliance_id):
    appliance = Appliance.objects.get(pk=appliance_id)
    if request.method == 'POST':
        form = ApplianceForm(request.POST, instance=appliance)
        if form.is_valid():
            form.save()
            return redirect('appliance-detail', pk=appliance.id)
    else:
        form = ApplianceForm(instance=appliance)
    return render(request, 'cooking/appliance_form.html', {'form': form, 'appliance': appliance})

def delete_appliance(request, appliance_id):
    # Handle deleting an appliance
    appliance = Appliance.objects.get(pk=appliance_id)
    if request.method == 'POST':
        appliance.delete()
        return redirect('appliance-list')
    return render(request, 'cooking/appliance_confirm_delete.html', {'appliance': appliance})

def create_ingredient(request):
    # Handle form submission to create a new ingredient
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save()
            return redirect('ingredient-detail', ingredient.id)
    else:
        form = IngredientForm()
    return render(request, 'cooking/ingredient_form.html', {'form': form})

def update_ingredient(request, ingredient_id):
    # Handle updating an existing ingredient
    ingredient = Ingredient.objects.get(pk=ingredient_id)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient-detail', ingredient.id)
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'cooking/ingredient_form.html', {'form': form, 'ingredient': ingredient})

def delete_ingredient(request, ingredient_id):
    # Handle deleting an ingredient
    ingredient = Ingredient.objects.get(pk=ingredient_id)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient-list')
    return render(request, 'cooking/ingredient_confirm_delete.html', {'ingredient': ingredient})

def index(request):
    return render(request, 'cooking/index.html')
    
class ApplianceListView(generic.ListView):
    model = Appliance
class ApplianceDetailView(generic.DetailView):
    model = Appliance
    template_name = 'cooking/appliance_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class IngredientListView(generic.ListView):
    model = Ingredient

class IngredientDetailView(generic.DetailView):
    model = Ingredient
    template_name = 'cooking/ingredient_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context