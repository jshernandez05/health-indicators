from health_indicators import __version__
from health_indicators import bmi


def test__version__():
    assert __version__ == "0.0.1"

def test_bmi():
    results = bmi(54, 1.70)
    assert results == 18