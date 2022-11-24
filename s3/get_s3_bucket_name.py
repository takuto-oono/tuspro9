from pathlib import Path
import environ
import os


def get_s3_bucket_name() -> str:
    env = environ.Env()
    env.read_env(os.path.join(Path(__file__).resolve(strict=True).parent.parent, '.env'))
    return env('AWS_STORAGE_BUCKET_NAME')


