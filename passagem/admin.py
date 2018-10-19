from django.contrib import admin
from .models import Hospital, HospMed, Paciente, Anotacao, Medico, Leito

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Paciente)

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    prepopulated_fields = {'user' : ('nome', )}

admin.site.register(Leito)
