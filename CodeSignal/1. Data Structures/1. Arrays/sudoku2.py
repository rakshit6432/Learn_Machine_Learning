import numpy as np
import itertools as it


def calculateDuplicate(listNum):
    duplicate = [1 for nums in listNum if (nums.isdecimal()) & (listNum.count(nums) > 1)]
    return duplicate


def sudoku2(grid):
    duplicateTotal = []

    # Transform grid to horizontal
    transformedGrid = (np.asarray(grid).T).tolist()

    # Checking for duplicates in horizontal and vertical lists
    for nums in it.chain(grid, transformedGrid):
        duplicateTotal.extend(calculateDuplicate(nums))
        if sum(duplicateTotal) > 1: break  # noqa E701

    # Checking diagonal duplicate only if horizontal & vertical test passess
    if sum(duplicateTotal) == 0:
        x1, x2 = range(3), range(3)
        diagonal = np.dsplit(np.asarray(grid).reshape(3, 3, 9), 3)
        for m, n in it.product(x1, x2):
            blank = []
            for o in range(3):
                blank.extend(diagonal[m][n][o].flatten())
            duplicateTotal.extend(calculateDuplicate(blank))
            if sum(duplicateTotal) > 1: break   # noqa E701

    # Final Check
    return True if sum(duplicateTotal) == 0 else False
