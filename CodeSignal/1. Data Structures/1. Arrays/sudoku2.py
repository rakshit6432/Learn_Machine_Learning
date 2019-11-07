import numpy as np


def calculateDuplicate(listNum):
    duplicate = [1 for nums in listNum if (nums.isdecimal()) & (listNum.count(nums) > 1)]
    return duplicate


def sudoku2(grid):
    duplicateTotal = []

    # Checking horizontal duplicate
    for i in grid:
        duplicateTotal.extend(calculateDuplicate(i))

    # Checking vertical duplicate only if horizontal test passess
    if sum(duplicateTotal) == 0:
        transformedGrid = (np.asarray(grid).T).tolist()
        for k in transformedGrid:
            duplicateTotal.extend(calculateDuplicate(k))

    # Checking diagonal duplicate only if horizontal & vertical test passess
    if sum(duplicateTotal) == 0:
        diagonal = np.dsplit(np.asarray(grid).reshape(3, 3, 9), 3)
        for m in range(3):
            for n in range(3):
                blank = []
                for o in range(3):
                    blank.extend(diagonal[m][n][o].flatten())
                duplicateTotal.extend(calculateDuplicate(blank))

    # Check diagonal test
    if sum(duplicateTotal) == 0:
        return True
    else:
        return False
