from pathlib import Path
import environ
import os
import sys


class ENV():
    def __init__(self) -> None:
        self.env = environ.Env()
        self.env.read_env(os.path.join(
            Path(__file__).resolve(strict=True).parent.parent, '.env'))

    def get_secret_key(self):
        return self.env('SECRET_KEY')

    def get_aws_access_key_id(self):
        return self.env('AWS_ACCESS_KEY_ID')

    def get_aws_secret_access_key(self):
        return self.env('AWS_SECRET_ACCESS_KEY')

    def get_aws_storage_bucket_name(self):
        return self.env('AWS_STORAGE_BUCKET_NAME')

    def get_aws_default_region(self):
        return self.env('AWS_DEFAULT_REGION')
