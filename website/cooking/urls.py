from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ingredients/', views.IngredientListView.as_view(), name='ingredient-list'),
    path('ingredient/<int:pk>/', views.IngredientDetailView.as_view(), name='ingredient-detail'),
    path('appliances/', views.ApplianceListView.as_view(), name='appliance-list'),
    path('appliance/<int:pk>/', views.ApplianceDetailView.as_view(), name='appliance-detail'),
    path('appliance/create_appliance/', views.create_appliance, name='create_appliance'),
    path('appliance/<int:appliance_id>/delete_appliance/', views.delete_appliance, name='delete_appliance'),
    path('appliance/<int:appliance_id>/update_appliance/', views.update_appliance, name='update_appliance'),
    path('ingredient/create_ingredient/', views.create_ingredient, name='create_ingredient'),
    path('ingredient/<int:ingredient_id>/delete_ingredient/', views.delete_ingredient, name='delete_ingredient'),
    path('ingredient/<int:ingredient_id>/update_ingredient/', views.update_ingredient, name='update_ingredient'),
]
