
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, Http404
from django.views.decorators.http import require_GET
from .models import WadaAlgorithm, MasahiroAlgorithm, YudaiAlgorithm
import datetime
from algorithm.alg_wada_main import alg_main


def index(request):
    return render(request, 'disneyapp/index.html')


@require_GET
def get_time_visiting_all_attractions(request: HttpRequest) -> JsonResponse:
    index = request.GET.get('index')
    model_list = [WadaAlgorithm, MasahiroAlgorithm, YudaiAlgorithm]
    model_id = request.GET.get('model_id')
    if not model_id:
        raise Http404
    print(model_id)
    model = model_list[int(model_id)]
    print(model)
    if not index:
        raise Http404
    date = datetime.date.today() + datetime.timedelta(days=int(index))
    try:
        object = model.objects.get(date=date)
        return JsonResponse({
            'status': 200,
            'time': object.time,
            'is_visit_all_attractions': object.is_visit_all_attractions,
            'date': date,
            'route': object.route,
        })
    except model.DoesNotExist:
        route, time = alg_main(date, 16, 0.2, 0.3)
        model.objects.create(
            date=date,
            time=time,
            is_visit_all_attractions=time <= 720,
            route=route,
        )
        return JsonResponse({
            'status': 200,
            'time': time,
            'is_visit_all_attractions': time <= 720,
            'date': date,
            'route': route,
        })