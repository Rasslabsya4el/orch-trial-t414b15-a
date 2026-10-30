import os


def test_added_by_p1():
    with open(os.environ['T414B_DATA']) as f:
        text = f.read()
    assert text.split()[0] in ('STUB', 'REAL')
