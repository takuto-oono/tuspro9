from django.contrib import admin
from .models import TimeVisitingAllAttractions


class TimeVisitingAllAttractionsAdmin(admin.ModelAdmin):
    list_display = ('date', 'time', 'route', 'is_visit_all_attractions')
    
admin.site.register(TimeVisitingAllAttractions, TimeVisitingAllAttractionsAdmin)
