
from pathlib import Path
import logging

from src.s3 import download, upload, DATA_PATH
log = logging.getLogger(__name__)


def clean():
    """Clean Content after UnitTests
    """
    for file in list(Path(DATA_PATH).resolve().parent.glob('*.json')):
        file.unlink()


def test_download():
    log.info("Downloading Storage File from last run")
    log.info(
        "If ERROR [400] is displayed, AccessToken is not Valid or AWS_PROFILE is not set.")
    log.info(
        "If ERROR [404] File is not in S3, Maybe first run?")
    clean()
    download()

    assert Path(DATA_PATH).is_file() == True, "Download failed"
    log.info("Completed")
