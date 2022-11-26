from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, Http404
from django.views.decorators.http import require_GET
from .models import TimeVisitingAllAttractions
import datetime
# Create your views here.


def index(request):
    return render(request, 'disneyapp/index.html')


@require_GET
def get_time_visiting_all_attractions(request: HttpRequest) -> JsonResponse:
    index = request.GET.get('index')
    if not index:
        raise Http404
    date = datetime.date.today() + datetime.timedelta(days=int(index))
    try:

        object = TimeVisitingAllAttractions.objects.get(date=date)
        return JsonResponse({
            'status': 200,
            'time': object.time,
            'is_visit_all_attractions': object.is_visit_all_attractions,
            'date': date,
            'route': [1, 2],
        })
    except TimeVisitingAllAttractions.DoesNotExist:
        #ここでアルゴリズムを実行したい
        
        TimeVisitingAllAttractions.objects.create(
            date=date,
            time=1000,
            is_visit_all_attractions=True,
            route=[1, 2, 3],
        )   
        return JsonResponse({
            'status': 200,
            'time': 1000,
            'is_visit_all_attractions': True,
            'date': date,
            'route': [1, 2, 3],
        })
