from util import s3
from typing import List, Tuple
import datetime
from algorithm.alg_util import wrapper_alg
from algorithm.alg_wada import IPSO


def alg_main(date: datetime.date, m: int, c1: float, c2: float) -> Tuple[List[int], int]:
    ipso = IPSO(m, c1, c2, display_flg=True)
    expected_wait_time_data = s3.get_csv_file(
        'expected_wait_time_data/expected_wait_time_data_{}.csv'.format(date.strftime('%Y%m%d')))
    attractions_distances = s3.get_csv_file('attractions_dis.csv')
    return wrapper_alg(ipso, attractions_distances, expected_wait_time_data, True)
