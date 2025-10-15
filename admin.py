from django.contrib import admin
from .models import Clientes

class ClientesAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'edad', 'email']
    list_display_links = ['id', 'nombre']
    search_fields = ['nombre', 'email']
    list_per_page = 20

admin.site.register(Clientes, ClientesAdmin)