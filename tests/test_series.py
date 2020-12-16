from math_series.series import fibonacci, lucas

def test_fibonacci():
    n = 4
    expected = 3
    actual = fibonacci(n)
    assert(actual == expected)

def test_lucas():
    n = 4
    expected = 4
    actual = lucas(n)
    assert(actual == expected)