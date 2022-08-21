from pathlib import Path


def clean():
    """Clean Content after UnitTests
    """
    for file in list(Path(__file__).resolve().parent.parent.glob('*_signed.pdf')):
        file.unlink()


def test_do():
    """This test is a dummy
    """

    assert False == True, "Test failed"
