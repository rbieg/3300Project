from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from .forms import IngredientForm, ApplianceForm, CreateUserForm, LoggedUserForm
from django.contrib import messages
from django.contrib.auth.models import Group
from .decorators import unauthenticatedUser, allowedUsers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.views import LoginView
from django.contrib.auth import authenticate, login

@login_required(login_url='login')
@allowedUsers(allowedRoles=['user_role'])
def create_appliance(request):
    if request.method == 'POST':
        form = ApplianceForm(request.POST)
        if form.is_valid():
            appliance = form.save()
            return redirect('appliance-detail', pk=appliance.id)
    else:
        # Retrieve form data from cookies
        form = ApplianceForm(initial={
            'name': request.COOKIES.get('name', ''),
            'description': request.COOKIES.get('description', ''),
            'heat_setting': request.COOKIES.get('heat_setting', ''),
        })
    return render(request, 'cooking/appliance_form.html', {'form': form})

@login_required(login_url='login')
@allowedUsers(allowedRoles=['user_role'])
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

@login_required(login_url='login')
@allowedUsers(allowedRoles=['user_role'])
def delete_appliance(request, appliance_id):
    # Handle deleting an appliance
    appliance = Appliance.objects.get(pk=appliance_id)
    if request.method == 'POST':
        appliance.delete()
        return redirect('appliance-list')
    return render(request, 'cooking/appliance_confirm_delete.html', {'appliance': appliance})

@login_required(login_url='login')
@allowedUsers(allowedRoles=['user_role'])
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

@login_required(login_url='login')
@allowedUsers(allowedRoles=['user_role'])
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

@login_required(login_url='login')
@allowedUsers(allowedRoles=['user_role'])
def delete_ingredient(request, ingredient_id):
    # Handle deleting an ingredient
    ingredient = Ingredient.objects.get(pk=ingredient_id)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient-list')
    return render(request, 'cooking/ingredient_confirm_delete.html', {'ingredient': ingredient})

def index(request):
    return render(request, 'cooking/index.html')
    
class ApplianceListView(LoginRequiredMixin, generic.ListView):
    model = Appliance
class ApplianceDetailView(LoginRequiredMixin, generic.DetailView):
    model = Appliance
    template_name = 'cooking/appliance_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
    
class IngredientListView(LoginRequiredMixin, generic.ListView):
    model = Ingredient

class IngredientDetailView(LoginRequiredMixin, generic.DetailView):
    model = Ingredient
    template_name = 'cooking/ingredient_detail.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@unauthenticatedUser
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('user')
            group = Group.objects.get(name='user_role')
            user.groups.add(group)
            loggedUser = LoggedUser.objects.create(user=user,)
            loggedUser.save()

            if username is not None: 
                messages.success(request, 'Account was created for ' + username)
            else:
                messages.success(request, 'Account was created successfully')
            return redirect('index')
    context = {'form':form}
    return render(request, 'registration/register.html', context)

@login_required(login_url='login')
@allowedUsers(allowedRoles=['user_role'])
def userPage(request):
    loggedUser = request.user.student
    form = LoggedUserForm(instance = loggedUser)
    print('loggedUser', loggedUser)
    if request.method == 'POST':
        form = LoggedUserForm(request.POST, request.FILES, instance=loggedUser)
        if form.is_valid():
            form.save()
        context = {'form':form}
        return render(request, 'cooking/user.html', context)

def set_cookie(request):
    response = HttpResponse("Cookie set successfully")
    response.set_cookie('my_cookie', 'cookie_value', max_age=3600, secure=True, httponly=True)
    return response

def get_cookie(request):
    cookie_value = request.COOKIES.get('my_cookie', 'default_value')
    return HttpResponse(f"Cookie value: {cookie_value}")