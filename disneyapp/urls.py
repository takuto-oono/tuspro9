from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_time_visiting_all_attractions/', views.get_time_visiting_all_attractions,
         name='get_time_visiting_all_attractions'),

]
