from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class TimeVisitingAllAttractions(models.Model):
    is_visit_all_attractions = models.BooleanField(default=False)
    time = models.IntegerField(default=-1)
    date = models.DateField()
    route = ArrayField(models.IntegerField())
    
    def __str__(self):
        return self.date

