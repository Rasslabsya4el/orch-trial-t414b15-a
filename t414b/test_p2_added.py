import os


def test_added_by_p2():
    with open(os.environ['T414B_DATA']) as f:
        text = f.read()
    assert not text.startswith('REAL'), 'the planted failure: only the real file fails it'
