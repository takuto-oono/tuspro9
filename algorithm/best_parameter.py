from algorithm import alg_main
import datetime
from typing import Tuple, List
from util import s3
import csv
import threading



def run_alg_wada_each_day(attractions_distances_data: List[List[int]], day: int) -> None:
    m_list = [16, 32, 64]
    c1_list = [i / 10 ** 1 for i in range(10)]
    c2_list = [i / 10 ** 1 for i in range(10)]
    k_list = [8 * i for i in range(1, 8)]

    date = datetime.date(year=2022, month=11, day=day)
    data = []
    error_list = []
    print('------------------------------get_s3_file-------------------------------------------------')
    wait_time_data = s3.get_csv_file(
        'wait_time_data/wait_time_data_{}.csv'.format(date.strftime('%Y%m%d')))
    print('-----------------------------------------------------------------------------------------')
    for m in m_list:
        for c1 in c1_list:
            for c2 in c2_list:
                for k in k_list:
                    if k > m - 1:
                        break

                    try:
                        _, time = alg_main.alg_main_wada(
                            attractions_distances=attractions_distances_data,
                            wait_time_data=wait_time_data,
                            m=m,
                            c1=c1,
                            c2=c2,
                            k=k,
                        )
                        print('--------------------------------' + str(date) + '-------------------------------')
                        print(date, m, c1, c2, k, time)
                        data.append([date, m, c1, c2, k, time])
                    except:
                        error_list.append([m, c1, c2, k])

    with open('../data/best_parameter_test/parameter_test_{}.csv'.format(date.strftime('%Y%m%d')), 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(data)

    with open('../data/error_list_best_parameter_test/parameter_test_{}.csv'.format(date.strftime('%Y%m%d')), 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(error_list)


def find_best_parameter_alg_wada() -> None:
    attractions_distances = s3.get_csv_file('attractions_distances_data.csv')
    for day in range(1, 31):
        run_alg_wada_each_day(attractions_distances_data=attractions_distances, day=day)
        
if __name__ == '__main__':
    find_best_parameter_alg_wada()
