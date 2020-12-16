from math_series.series import fibonacci

def test_fibonacci():
    n = 4
    expected = 3
    actual = fibonacci(n)
    assert(actual == expected)

