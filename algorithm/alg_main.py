from util import s3
from typing import List, Tuple
import datetime
from algorithm import alg_wada, alg_util, alg_kondo


def alg_main_wada(date: datetime.date, m: int, c1: float, c2: float) -> Tuple[List[int], int]:
    ipso = alg_wada.IPSO(m, c1, c2, display_flg=True)
    expected_wait_time_data = s3.get_csv_file(
        'expected_wait_time_data/expected_wait_time_data_{}.csv'.format(date.strftime('%Y%m%d')))
    attractions_distances = s3.get_csv_file('attractions_distances_data.csv')
    return alg_util.wrapper_alg(ipso, attractions_distances, expected_wait_time_data, True)


def alg_main_yudai(date: datetime.date) -> Tuple[List[int], int]:
    print('in main func')
    expected_wait_time_data = s3.get_csv_file(
        'expected_wait_time_data/expected_wait_time_data_{}.csv'.format(date.strftime('%Y%m%d')))
    attractions_distances = s3.get_csv_file('attractions_distances_data.csv')
    return alg_util.wrapper_alg(alg_kondo.CRIST(), attractions_distances, expected_wait_time_data, False)


# if __name__ == '__main__':
#     alg_main_wada(date=datetime.date(2022, 11, 25), 16, 0.2, 0.3)
