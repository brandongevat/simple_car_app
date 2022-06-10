from django.contrib import admin
from .models import Engine, Make, Car

# Register your models here.
@admin.register(Engine, Make, Car)
class CarAdmin(admin.ModelAdmin):
    pass