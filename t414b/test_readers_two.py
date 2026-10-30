import os
from pathlib import Path


def test_reader_two():
    assert Path(os.environ["T414B_DATA"]).read_text().split()[0] in ("STUB", "REAL")
