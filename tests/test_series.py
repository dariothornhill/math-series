from math_series.series import fibonacci, lucas, sum_series

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

def test_sum_series_lucas():
    n = 4
    expected = 4
    actual = sum_series(n, 2, 1)
    assert(actual == expected)

def test_sum_series_fib():
    n = 4
    expected = 3
    actual = sum_series(n)
    assert(actual == expected)