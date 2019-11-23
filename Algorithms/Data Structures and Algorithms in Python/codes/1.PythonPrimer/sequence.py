"""
Write a short Python function that takes a sequence of integer values
and determines if there is a distinct pair of numbers in the sequence whose product is odd.
"""


def sequence(nums):
    # You have to have two odd number to get an odd from multiplying two numbers, using that to solve the problem
    set_nums = list(set(nums))
    if (len(set_nums) == (1 or 0)):
        return False
    return sum(1 for i in set_nums if (i%2==1)) >= 2


# flake8: noqa
def test_sequence():
    assert sequence([]) == False
    assert sequence([1,5]) == True
    assert sequence([2, 5]) == False
    assert sequence([3, 3]) == False
    assert sequence([5, 3]) == True
    assert sequence([2, 4, 2, 4, 5]) == False
    assert sequence([8, 4, 3, 3, 5]) == True
    assert sequence([3, 2, 5]) == True
    assert sequence([3, 2, 5, 9, 8]) == True


test_sequence()
