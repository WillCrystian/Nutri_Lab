from django.contrib import admin
from .models import Pacientes, DadosPaciente, Refeicao, Opcao

# Register your models here.

admin.site.register(Pacientes)
admin.site.register(DadosPaciente)
admin.site.register(Refeicao)
admin.site.register(Opcao)
