from typing import List
import datetime
from s3.get_csv_file import get_csv_file


def create_csv_file_wait_time_expect(year: int, month: int, day: int) -> List[List[int]]:
    today = datetime.datetime(
        year=year,
        month=month,
        day=day
    )
    get_csv_file(file_path='')
    