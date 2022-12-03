
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, Http404
from django.views.decorators.http import require_GET
from .models import WadaAlgorithm, MasahiroAlgorithm, YudaiAlgorithm
import datetime
from algorithm import alg_main
from django.db import connection


def index(request):
    return render(request, 'disneyapp/index.html')


@require_GET
def get_time_visiting_all_attractions(request: HttpRequest) -> JsonResponse:
    index = request.GET.get('index')
    model_list = [WadaAlgorithm, YudaiAlgorithm, MasahiroAlgorithm]
    model_id = request.GET.get('model_id')
    if not model_id:
        raise Http404
    model = model_list[int(model_id)]
    if not index:
        raise Http404
    date = datetime.date.today() + datetime.timedelta(days=int(index))
    test = WadaAlgorithm
    try:
        # object = model.objects.get(date=date)
        object = 0
        if model_id == '0':
            object = model.objects.raw(
                'SELECT * FROM disneyapp_wadaalgorithm WHERE date=%s', [str(date)])[0]
        elif model_id == '1':
            object = model.objects.raw(
                'SELECT * FROM disneyapp_yudaialgorithm WHERE date=%s', [str(date)])[0]
        else:
            object = model.objects.raw(
                'SELECT * FROM disneyapp_masahiroalgorithm WHERE date=%s', [str(date)])[0]

        # with connection.cursor() as cursor:
        #     cursor.execute('SELECT * FROM WadaAlgorithm WHERE time=%s', ['477'])
        #     data = cursor.fetchall()

        return JsonResponse({
            'status': 200,
            'time': object.time,
            'is_visit_all_attractions': object.is_visit_all_attractions,
            'date': date,
            'route': object.route,
        })
    except model.DoesNotExist:
        route, time = [], -1
        if model_id == '0':
            route, time = alg_main.alg_main_wada(date, 16, 0.2, 0.3)
        elif model_id == '1':
            route, time = alg_main.alg_main_yudai(date)
        elif model_id == '2':
            pass
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
