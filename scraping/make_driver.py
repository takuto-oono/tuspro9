from bs4 import BeautifulSoup
import os
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import time
from typing import List
import csv
from webdriver_manager.firefox import GeckoDriverManager

def make_driver():
    # Firefox のオプションを設定する
    # options = FirefoxOptions()
    # options.add_argument('--headless')
    # options.add_argument('--no-sandbox')
    # options.add_argument('--disable-dev-shm-usage')

    # Selenium Server に接続する
    # driver = webdriver.Firefox(
    #     # executable_path='./Disney/geckodriver',
    #     executable_path='./geckodriver',
    #     options=options,
    # )
    # return driver

    opts = FirefoxOptions()
    opts.add_argument("--headless")
    fox = webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=opts)
    return fox
    
    
    
    
if __name__ == '__main__':
    make_driver()
    