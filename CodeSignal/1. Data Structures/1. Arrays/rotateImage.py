# My Faster Numpy Solution
import numpy as np


def rotateImage(a):
    return (np.rot90(np.asarray(a), 3).tolist())


# Python solution without numpy
def rotateImageShort(a):
    return list(zip(*reversed(a)))
