from util.create_wait_time_all_atractions_csv_file import create_wait_time_all_attractions_csv_file
from util.create_expected_wait_time_csv_file import create_expected_wait_time_csv_file
import datetime


if __name__ == '__main__':
    date = datetime.date.today() - datetime.timedelta(days=1)
    create_wait_time_all_attractions_csv_file(
        year=date.year, month=date.month, day=date.day)
    date = datetime.date.today() + datetime.timedelta(days=6)
    create_expected_wait_time_csv_file(
        year=date.year, month=date.month, day=date.day)
