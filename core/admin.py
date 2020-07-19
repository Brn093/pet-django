from django.contrib import admin
from .models import Pet

# Register your models here.

# Registrando no sistema de adminstração o app criado
@admin.register(Pet)    # decorator com o registro da classe PET
class PetAdmin(admin.ModelAdmin):
    list_display = ['id', 'cidade', 'telefone', 'usuario'] # campos de registros visíveis para o administrador
