import os


def test_reader_one():
    with open(os.environ["T414B_DATA"]) as f:
        assert f.read().split()[0] in ("STUB", "REAL")
