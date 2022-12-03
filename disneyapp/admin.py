from django.contrib import admin
from .models import WadaAlgorithm, YudaiAlgorithm, MasahiroAlgorithm


class WadaAlgorithmAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'route', 'is_visit_all_attractions')
    
admin.site.register(WadaAlgorithm, WadaAlgorithmAdmin)

class YudaiAlgorithmAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'route', 'is_visit_all_attractions')
    
admin.site.register(YudaiAlgorithm, YudaiAlgorithmAdmin)

class MasahiroAlgorithmAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'route', 'is_visit_all_attractions')
    
admin.site.register(MasahiroAlgorithm, MasahiroAlgorithmAdmin)
