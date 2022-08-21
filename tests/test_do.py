from pathlib import Path
from s3 import download, upload


def clean():
    """Clean Content after UnitTests
    """
    for file in list(Path(__file__).resolve().parent.parent.glob('*_signed.pdf')):
        file.unlink()


def test_do():
    """This test is a dummy
    """

    assert False == True, "Test failed"


def test_download_s3():
    print("Downloading Storage File from last run")
    print(
        "If ERROR [400] is displayed, AccessToken is not Valid or AWS_PROFILE is not set.")
    print(
        "If ERROR [404] File is not in S3, Maybe first run?")
    # download()
    upload()
    print("Completed")
