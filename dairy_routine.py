from util.create_wait_time_all_atractions_csv_file import create_wait_time_all_attractions_csv_file
from util.create_expected_wait_time_csv_file import create_expected_wait_time_csv_file
import datetime
import time


if __name__ == '__main__':
    today = datetime.date.today()
    create_wait_time_all_attractions_csv_file(
        year=today.year, month=today.month, day=today.day)
    time.sleep(5)
    create_expected_wait_time_csv_file(
        year=today.year, month=today.month, day=today.day)
