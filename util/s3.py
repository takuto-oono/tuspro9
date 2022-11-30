from util.env import ENV
from typing import List
import boto3
import csv


def get_csv_file(file_path: str) -> List[List[int]]:
    try:
        s3_response = boto3.client('s3').get_object(
            Bucket=ENV().get_aws_storage_bucket_name(), Key='csv_data/{}'.format(file_path)
        )
        csv_data = s3_response['Body'].read().decode('utf-8').splitlines()
        result = [list for list in csv.reader(csv_data)]
        return [[int(result[i][j]) for j in range(len(result[i]))] for i in range(len(result))]
    except ValueError:
        print('not convert str to int')
        return [[]]
    except:
        print('not find {}'.format(file_path))
        return [[]]


def upload_file(local_file_path: str, file_path: str) -> None:
    env = ENV()
    session = boto3.Session(
    aws_access_key_id=env.get_aws_access_key_id(),
    aws_secret_access_key=env.get_aws_secret_access_key(),
    )
    s3 = session.resource('s3')
    s3.meta.client.upload_file(Filename=local_file_path, Bucket=env.get_aws_storage_bucket_name(), Key='csv_data/{}'.format(file_path))

if __name__ == '__main__':
    # upload_file('../attractions_distances_data.csv', 'attractions_dis.csv')
    print(get_csv_file('attractions_dis.csv'))