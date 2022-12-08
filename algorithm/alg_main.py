from typing import List, Tuple
import datetime
from algorithm import alg_wada, alg_util, alg_kondo, alg_masahiro


def alg_main_wada(attractions_distances: List[List[int]], wait_time_data: List[List[int]], m: int, c1: float, c2: float, k: int) -> Tuple[List[int], int]:
    ipso = alg_wada.IPSO(m, c1, c2, display_flg=True)
    return alg_util.wrapper_alg(ipso, attractions_distances, wait_time_data, True)


def alg_main_yudai(attractions_distances: List[List[int]], expected_wait_time_data: List[List[int]]) -> Tuple[List[int], int]:
    return alg_util.wrapper_alg(alg_kondo.CRIST(), attractions_distances, expected_wait_time_data, False)

def alg_main_masahiro(attractions_distances: List[List[int]], expected_wait_time_data: List[List[int]]) -> Tuple[List[int], int]:
    return alg_util.wrapper_alg(alg_masahiro.HOGE(), attractions_distances, expected_wait_time_data, True, True)


def alg_main_wada_2(attractions_distances: List[List[int]], wait_time_data: List[List[int]], m: int, e: int, cr: float, mr: float, c_alg: str) -> Tuple[List[int], int]:
    ga = alg_wada.GA(m, e, cr, mr, c_alg)
    return alg_util.wrapper_alg(ga, attractions_distances, wait_time_data, True)
