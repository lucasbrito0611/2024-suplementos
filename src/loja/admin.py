from django.contrib import admin
from .models import *

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('Nome', 'Email', 'CPF', 'Telefone_celular', 'Telefone_fixo', 'Dt_nasc')
    empty_value_display = 'Vazio'

admin.site.register(Cliente, ClienteAdmin)