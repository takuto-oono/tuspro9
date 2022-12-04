
from django.shortcuts import render
from django.http import HttpRequest, JsonResponse, Http404
from django.views.decorators.http import require_GET
from .models import WadaAlgorithm, YudaiAlgorithm, MasahiroAlgorithm
import datetime
from algorithm import alg_main
from django.db import connection
from util import s3


def index(request):
    return render(request, 'disneyapp/index.html')


@require_GET
def get_time_visiting_all_attractions(request: HttpRequest) -> JsonResponse:
    model_id = request.GET.get('model_id')
    if not model_id:
        raise Http404
    start_date = datetime.date.today()
    end_date = start_date + datetime.timedelta(days=6)

    response_dic = {i: {} for i in range(7)}
    algorithm_outputs = []
    if model_id == '0':
        algorithm_outputs = WadaAlgorithm.objects.raw(
            'SELECT * FROM disneyapp_wadaalgorithm WHERE date between %s and %s ORDER BY date ASC', [str(start_date), str(end_date)])
    
    if model_id == '1':
        algorithm_outputs = YudaiAlgorithm.objects.raw(
            'SELECT * FROM disneyapp_yudaialgorithm WHERE date between %s and %s ORDER BY date ASC', [str(start_date), str(end_date)])
    
    if model_id == '2':
        algorithm_outputs = MasahiroAlgorithm.objects.raw(
            'SELECT * FROM disneyapp_masahiroalgorithm WHERE date between %s and %s ORDER BY date ASC', [str(start_date), str(end_date)])
        
    if len(algorithm_outputs) == 7:
        for i, algorithm_output in enumerate(algorithm_outputs):
            response_dic[i] = {
                'time': algorithm_output.time,
                'is_visit_all_attractions': algorithm_output.is_visit_all_attractions,
                'date': algorithm_output.date,
                'route': algorithm_output.route,
            }
        return JsonResponse(response_dic)

    for algorithm_output in algorithm_outputs:
        for j in range(7):
            if start_date + datetime.timedelta(days=j) == algorithm_output.date:
                response_dic[j] = {
                    'time': algorithm_output.time,
                    'is_visit_all_attractions': algorithm_output.is_visit_all_attractions,
                    'date': algorithm_output.date,
                    'route': algorithm_output.route,
                }
                break

    attractions_distances = s3.get_csv_file('attractions_distances_data.csv')
    for key, item in response_dic.items():
        if item == {}:
            date = start_date + datetime.timedelta(days=key)
            expected_wait_time_data = s3.get_csv_file(
                'expected_wait_time_data/expected_wait_time_data_{}.csv'.format(date.strftime('%Y%m%d')))
            route, time = [], 0
            if model_id == '0':
                route, time = alg_main.alg_main_wada(attractions_distances, expected_wait_time_data,16, 0.2, 0.3)
                WadaAlgorithm.objects.create(
                    date=date,
                    time=time,
                    route=route,
                    is_visit_all_attractions=(time <= 720),
                )
                
            if model_id == '1':
                route, time = alg_main.alg_main_yudai(attractions_distances, expected_wait_time_data)
                YudaiAlgorithm.objects.create(
                    date=date,
                    time=time,
                    route=route,
                    is_visit_all_attractions=(time <= 720),
                )
                
            if model_id == '2':
                #　アルゴリズム実行分を書く
                MasahiroAlgorithm.objects.create(
                    date=date,
                    time=time,
                    route=route,
                    is_visit_all_attractions=(time <= 720),
                )
                
            response_dic[key] = {
                'time': time,
                'is_visit_all_attractions': time <= 720,
                'date': date,
                'route': route,
            }
    return JsonResponse(response_dic)
