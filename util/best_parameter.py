from algorithm import alg_main
import datetime
from typing import Tuple


def find_best_parameter_alg_wada(date: datetime.date) -> Tuple[float, float]:
    c1_list = [i / 10 ** 1 for i in range(10 ** 1)]
    c2_list = [i / 10 ** 1 for i in range(10 ** 1)]
    min_time = 10 ** 10
    best_c1, best_c2 = 0, 0
    error_list = []
    for c1 in c1_list:
        for c2 in c2_list:
            if c1 + c2 > 1:
                continue
            (_, time) = alg_main.alg_main_wada(date=date, m=16, c1=c1, c2=c2)
            if time < min_time:
                best_c1, best_c2 = c1, c2
                min_time = time
            print(c1, c2)
    return (best_c1, best_c2)


if __name__ == '__main__':
    date = datetime.date(year=2022, month=11, day=28)
    find_best_parameter_alg_wada(date)


