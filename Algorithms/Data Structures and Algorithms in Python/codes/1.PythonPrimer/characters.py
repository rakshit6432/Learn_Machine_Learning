"""
Demonstrate how to use Python’s list comprehension syntax to produce the list ['a', 'b', 'c', ..., 'z'],
but without having to type all 26 such characters literally.
"""


def characters():
    return [chr(97 + i) for i in range(26)]


# flake8: noqa
def test_characters():
    assert characters() == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


test_characters()
