from pathlib import Path
import sys
import os
import copy
from typing import List
import csv
import datetime
from util import s3


def create_expected_wait_time_csv_file(year: int, month: int, day: int) -> List[List[int]]:
    # -1の数をカウントしておく
    collecting_data_num = [[0 for _ in range(36)] for _ in range(48)]
    # 結果を格納するフォルダ
    expected_wait_time_list = [[0 for _ in range(36)] for _ in range(48)]
    base_day = datetime.date(
        year=year,
        month=month,
        day=day
    )

    s3_base_path = 'wait_time_data/wait_time_data_{}.csv'
    for i in range(4):
        sample_date = base_day - datetime.timedelta(days=7 * (i + 1))
        print(sample_date)

        # amazon s3からフィアルを取得する
        wait_time_data = s3.get_csv_file(
            'wait_time_data/wait_time_data_{}.csv'.format(sample_date.strftime('%Y%m%d')))

        # s3からのファイル取得が失敗している場合の処理
        if wait_time_data == [[]]:
            continue

        for j in range(len(wait_time_data)):
            for k in range(len(wait_time_data[j])):
                if wait_time_data[j][k] != -1:
                    collecting_data_num[j][k] += 1
                    expected_wait_time_list[j][k] += wait_time_data[j][k]

    for i in range(48):
        for j in range(36):
            # 4回とも-1なら-1を返す
            if collecting_data_num[i][j] == 0:
                expected_wait_time_list[i][j] = -1
            else:
                expected_wait_time_list[i][j] //= collecting_data_num[i][j]
    write_list = copy.deepcopy(expected_wait_time_list)
    with open('./data/expect_wait_time_data/expected_wait_time_data_' + base_day.strftime('%Y%m%d') + '.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(write_list)
    s3.upload_file('./data/expect_wait_time_data/expected_wait_time_data_{}.csv'.format(base_day.strftime('%Y%m%d')),
                   'expected_wait_time_data/expected_wait_time_data_{}.csv'.format(base_day.strftime('%Y%m%d')))
    return expected_wait_time_list


if __name__ == '__main__':
    today = datetime.date.today()
    # for i in range(7):
    #     date = today + datetime.timedelta(days=i)
    #     create_expected_wait_time_csv_file(date.year, date.month, date.day)
    create_expected_wait_time_csv_file(2022, 12, 5)
    create_expected_wait_time_csv_file(2022, 12, 2)
    create_expected_wait_time_csv_file(2022, 12, 3)
