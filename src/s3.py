import boto3
import os

import logging
log = logging.getLogger()

DEBUG = os.environ.get('DEBUG', None)
BUCKET = os.environ["BUCKET_NAME"]
log.info("Debug: {}".format(str(DEBUG)))
DATA_PATH = os.environ["SESSION_STORAGE"]

if DEBUG:
    debug_session = boto3.Session(profile_name=os.environ["AWS_PROFILE"])
    client = debug_session.client('s3')
else:
    client = boto3.client('s3')

log.info("Using target filepath {}".format(DATA_PATH))
log.info("Using target Bucket {}".format(BUCKET))


def upload():
    log.info("Uploading File")
    client.upload_file(DATA_PATH, BUCKET, "vacancies.json")


def download():
    log.info("Downloading File")
    try:
        client.download_file(BUCKET, "vacancies.json", DATA_PATH)
    except:
        log.warning(
            "Could not download file from S3 Bucket, maybe first run?", exc_info=True)
