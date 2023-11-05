from django.contrib import admin
from .models import Appliance
from .models import Ingredient



# Register your models here so they can be edited in admin panel
admin.site.register(Appliance)
admin.site.register(Ingredient)