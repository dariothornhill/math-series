from math_series.series import fibonacci, lucas, sum_series
import pytest


def test_fibonacci(fib_fixture):
    for pair in fib_fixture:
        n = pair[0]
        expected = pair[1]
        actual = fibonacci(n)
        assert actual == expected


def test_lucas(lucas_fixture):
    for pair in lucas_fixture:
        n = pair[0]
        expected = pair[1]
        actual = lucas(n)
        assert actual == expected


def test_sum_series_fib(fib_fixture):
    for pair in fib_fixture:
        n = pair[0]
        expected = pair[1]
        actual = sum_series(n)
        assert actual == expected


def test_sum_series_lucas(lucas_fixture):
    for pair in lucas_fixture:
        n = pair[0]
        expected = pair[1]
        actual = sum_series(n, 2, 1)
        assert actual == expected


@pytest.fixture
def lucas_fixture():
    return [(0, 2), (1, 1), (2, 3), (3, 4), (4, 7), (5, 11)]


@pytest.fixture
def fib_fixture():
    return [(0, 0), (1, 1), (2, 1), (3, 2), (4, 3), (5, 5)]
