from django.contrib import admin
from .models import WadaAlgorithm


class WadaAlgorithmAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'route', 'is_visit_all_attractions')
    
admin.site.register(WadaAlgorithm, WadaAlgorithmAdmin)
