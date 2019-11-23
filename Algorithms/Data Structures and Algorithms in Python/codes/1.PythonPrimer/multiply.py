"""
Write a short Python function, is multiple(n, m), that takes two integer values
and returns True if n is a multiple of m, that is, n = mi for some integer i, and False otherwise.
"""

def multiply(n, m):
    if n == 0:
        return False
    return (n/m).is_integer()


# flake8: noqa
def test_multiply():
    assert multiply(0, 2) == False
    assert multiply(4, 2) == True
    assert multiply(8, 2) == True
    assert multiply(-8, 2) == True
    assert multiply(7, 2) == False


test_multiply()
