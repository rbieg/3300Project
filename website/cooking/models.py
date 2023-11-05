from django.db import models
from django.urls import reverse

# Create your models here.
class Appliance(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200, blank=True)
    heat_setting_choices = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', "High"),
        # Add more settings if needed
        ]

    heat_setting = models.CharField(max_length=20, choices=heat_setting_choices, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("appliance-detail", args=[str(self.id)])
    
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30, blank=True)
    
    cooking_method_choices = [
        ('baking', 'Baking'),
        ('grilling', 'Grilling'),
        ('sautéing', 'Sautéing'),
        ('boiling', 'Boiling'),
        ('microwaving', 'Microwaving'),
        # Add more cooking methods as needed
    ]

    cooking_method = models.CharField(max_length=20, choices=cooking_method_choices, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("ingredient-detail", args=[str(self.id)])

# class UnloggedUser(models.Model):
#    TBI
    

# class LoggedUser(models.Model):
#     username = models.CharField(max_length=30)
#     email    = models.CharField(max_length=200) 
#     password = models.CharField(max_length=20)

# class Recipe(models.Model):
#    TBI