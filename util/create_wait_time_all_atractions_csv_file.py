from typing import List
import csv
import time
from bs4 import BeautifulSoup
import os
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.firefox import GeckoDriverManager
from util import s3


def make_driver():
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    fox = webdriver.Firefox(
        executable_path=GeckoDriverManager().install(), options=opts)
    return fox


def create_wait_time_all_attractions_csv_file(year: int, month: int, day: int) -> List[List[int]]:
    def create_xpath_by_a(index: int) -> str:
        return '/html/body/div[3]/div[1]/article/table[2]/tbody/tr[' + str(index + 2) + ']/td[2]/a'

    def create_xpath_by_td(index: int) -> str:
        return '/html/body/div[3]/div[1]/article/table[2]/tbody/tr[' + str(index + 2) + ']/td[1]'

    driver = make_driver()
    m = str(month)
    d = str(day)
    if len(m) == 1:
        m = '0' + m
    if len(d) == 1:
        d = '0' + d
    date_str = str(year) + m + d

    driver.get('https://urtrip.jp/tdl-past-info/?rm=' + date_str + '#cal')
    print('access' + date_str)

    wait_time_list = []
    xpath_list = [
        '//*[@id="post-62757"]/article/div[2]/div/div[3]/table/tbody/tr',
        '//*[@id="post-62757"]/article/div[2]/div/div[4]/table/tbody/tr',
        '//*[@id="post-62757"]/article/div[2]/div/div[5]/table/tbody/tr',
        '//*[@id="post-62757"]/article/div[2]/div/div[6]/table/tbody/tr',
        '//*[@id="post-62757"]/article/div[2]/div/div[7]/table/tbody/tr',
    ]

    for i in range(48):
        wait_times = []
        for j in range(5):
            wait_times += driver.find_element(
                by='xpath', value=xpath_list[j] + '[' + str(i + 2) + ']').text.split()[1:]
        wait_time_list.append(wait_times)
    print(wait_time_list)
    for i in range(len(wait_time_list)):
        for j in range(len(wait_time_list[i])):
            try:
                wait_time_list[i][j] = int(wait_time_list[i][j])
            except:
                wait_time_list[i][j] = -1

    with open('./data/wait_time_csv_files/wait_time_data_' + date_str + '.csv', 'w') as file:
        writer = csv.writer(file, lineterminator='\n')
        writer.writerows(wait_time_list)
    print(len(wait_time_list))
    print(len(wait_time_list[0]))
    driver.close()
    file_name = 'wait_time_data_' + date_str + '.csv'

    s3.upload_file('./data/wait_time_csv_files/wait_time_data_{}.csv'.format(date_str),
                   'wait_time_data/' + file_name)
    return wait_time_list


if __name__ == '__main__':
    create_wait_time_all_attractions_csv_file(2022, 10, 23)
