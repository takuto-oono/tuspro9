from alg_wada import IPSO
from alg_util import wrapper_alg
import datetime
from typing import List, Tuple


def shape_dist(source: str) -> list[list[int]]:
    dist = []
    with open(source, 'r') as f:
        dist = f.read().split('\n')
    dist = [x.split(',') for x in dist][:-1]
    dist = [[int(x) for x in l] for l in dist]
    return dist


def alg_main(date: datetime.date) -> Tuple[List[int], int]:
    ipso = IPSO(16, 0.2, 0.3, display_flg=True)
    attractions_distances = shape_dist('../attractions_distances_data.csv')
    wait_time_data = shape_dist(
        '../data/wait_time_csv_files/wait_time_data_{}.csv'.format(date.strftime('%Y%m%d')))
    return wrapper_alg(ipso, attractions_distances, wait_time_data, True)


if __name__ == '__main__':
    alg_main(datetime.date(2022, 11, 25))
