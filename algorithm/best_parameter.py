from algorithm import alg_main
import datetime
from typing import Tuple, List
from util import s3
import csv


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
                        print('--------------------------------' +
                              str(date) + '-------------------------------')
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
        run_alg_wada_each_day(
            attractions_distances_data=attractions_distances, day=day)


def find_best_parameter_alg_wada_2() -> None:
    attractions_distances = s3.get_csv_file('attractions_distances_data.csv')
    for day in range(1, 31):
        run_ga_each_day(
            attractions_distances_data=attractions_distances, day=day)


def find_best_parameter_2() -> None:
    mapping_index = []
    m_list = [16, 32, 64, 128]
    e_list = [2, 4, 6, 8, 12, 16, 28, 32]
    cr_list = [1.0, 0.9, 0.8, 0.7]
    mr_list = [i / 10 for i in range(11)]
    c_alg_list = ['CX', 'CX2', 'CX3']
    data = []
    for m in m_list:
        for e in e_list:
            for cr in cr_list:
                for mr in mr_list:
                    for c_alg in c_alg_list:
                        mapping_index.append([str(m), str(e), str(cr), str(mr), c_alg])
                        data.append([0, 0])
    for day in range(1, 8):
        with open('../data/best_parameter_test_2/parameter_test_{}_2.csv'.format(datetime.date(year=2022, month=11, day=day).strftime('%Y%m%d'))) as f:
            reader = csv.reader(f)
            for row in reader:
                list = row[1:6]
                for i, l in enumerate(mapping_index):
                    if l == list:
                        data[i][0] += int(row[6])
                        data[i][1] += 1

    for i in range(len(data)):
        if data[i][1] == 0:
            continue
        data[i][0] /= data[i][1]
        if data[i][1] != 7:
            data[i][0] = 10 ** 10

    min_time = 10 ** 5
    index = 0
    for i, v in enumerate(data):
        if min_time > data[i][0] and data[i][0] != 0:
            min_time = data[i][0]
            index = i
        print(min_time)

    print(mapping_index[index])

def find_best_parameter() -> None:
    mapping_index = []
    m_list = [16, 32, 64]
    c1_list = [i / 10 ** 1 for i in range(10)]
    c2_list = [i / 10 ** 1 for i in range(10)]
    k_list = [8 * i for i in range(1, 8)]
    data = []
    for m in m_list:
        for c1 in c1_list:
            for c2 in c2_list:
                for k in k_list:
                    if k <= m - 1:
                        mapping_index.append(
                            [str(m), str(c1), str(c2), str(k)])
                        data.append([0, 0])

    for day in range(1, 31):
        with open('../data/best_parameter_test/parameter_test_{}.csv'.format(datetime.date(year=2022, month=11, day=day).strftime('%Y%m%d'))) as f:
            reader = csv.reader(f)
            for row in reader:
                list = [row[1], row[2], row[3], row[4]]
                for i, l in enumerate(mapping_index):
                    if l == list:

                        data[i][0] += int(row[5])
                        data[i][1] += 1

    for i in range(len(data)):
        if data[i][1] == 0:
            continue
        data[i][0] /= data[i][1]
        if data[i][1] != 28:
            data[i][0] = 10 ** 10

    min_time = 10 ** 5
    index = 0
    for i, v in enumerate(data):
        if min_time > data[i][0] and data[i][0] != 0:
            min_time = data[i][0]
            index = i
        print(data[i][0])

    print(mapping_index[index])

def run_ga_each_day(attractions_distances_data: List[List[int]], day: int) -> None:
    m_list = [16, 32, 64, 128]
    e_list = [2, 4, 8, 16, 32]
    cr_list = [1.0, 0.9, 0.8]
    mr_list = [i / 10 for i in range(11) if i % 3 == 0]
    c_alg_list = ['CX', 'CX2', 'CX3']
    date = datetime.date(year=2022, month=11, day=day)
    data = []
    error_list = []
    print('------------------------------get_s3_file-------------------------------------------------')
    wait_time_data = s3.get_csv_file(
        'wait_time_data/wait_time_data_{}.csv'.format(date.strftime('%Y%m%d')))
    print('-----------------')

    for m in m_list:
        for e in e_list:
            if e < m / 4 + 1:
                for cr in cr_list:
                    for mr in mr_list:
                        for c_alg in c_alg_list:
                            try:
                                _, time = alg_main.alg_main_wada_2(
                                    attractions_distances=attractions_distances_data,
                                    wait_time_data=wait_time_data,
                                    m=m,
                                    e=e,
                                    cr=cr,
                                    mr=mr,
                                    c_alg=c_alg,
                                )
                                data.append([date, m, e, cr, mr, c_alg, time])
                                print(date, m, e, cr, mr, c_alg, time)
                            except:
                                error_list.append([date, m, e, cr, mr, c_alg])

    with open('../data/best_parameter_test_2/parameter_test_{}_2.csv'.format(date.strftime('%Y%m%d')), 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(data)

    if error_list:
        with open('../data/error_list_best_parameter_test_2/parameter_test_{}_2.csv'.format(date.strftime('%Y%m%d')), 'w') as file:
            writer = csv.writer(file, lineterminator='\n')
            writer.writerows(error_list)


if __name__ == '__main__':
    # find_best_parameter_alg_wada()
    # find_best_parameter()
    # find_best_parameter_alg_wada_2()
    find_best_parameter_2()
