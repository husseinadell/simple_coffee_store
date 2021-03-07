from django.contrib import admin
from .models import CoffeeMachine, CoffeePod
# Register your models here.

admin.site.register(CoffeeMachine)
admin.site.register(CoffeePod)