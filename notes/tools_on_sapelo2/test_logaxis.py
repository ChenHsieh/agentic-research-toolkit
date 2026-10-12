import numpy as np
from logaxis import fmt_decade, log10p

def test_fmt_decade():
    assert fmt_decade(0) == "0"
    assert fmt_decade(1) == "1"
    assert fmt_decade(10) == "10"
    assert fmt_decade(1000) == "1k"
    assert fmt_decade(1500) == "1.5k"
    assert fmt_decade(1e6) == "1M"
    assert fmt_decade(2e9) == "2B"
    assert fmt_decade(0.1) == "0.1"
    assert fmt_decade(0.001) == "0.001"
    assert fmt_decade(-1000) == "-1k"

def test_log10p():
    assert abs(log10p(0) - 0) < 1e-12
    assert abs(log10p(9) - 1) < 1e-12
    assert abs(log10p(99, c=1) - 2) < 1e-12
    arr = log10p([0, 9])
    expected = np.array([0.0, 1.0])
    assert np.allclose(arr, expected, atol=1e-12)

if __name__ == "__main__":
    test_fmt_decade()
    test_log10p()
    print("ALL PASS")
