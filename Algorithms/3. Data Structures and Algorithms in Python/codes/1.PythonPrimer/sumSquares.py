"""
Write a short Python function that takes a positive integer n
and returns the sum of the squares of all the positive integers smaller than n.
"""


def sum_squares(n):
    if n < 0:
        print("Please input a positive integer")
    return sum(map(lambda x: x**2, range(n + 1)))


def test_sum_squares():
    assert (sum_squares(2) == 5)
    assert (sum_squares(5) == 55)
    assert (sum_squares(9) == 285)


test_sum_squares()
