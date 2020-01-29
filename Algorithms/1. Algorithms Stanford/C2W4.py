#2sum algorithm

import bisect

input_array = []
split_inv = 0


def merge(left, right):
    global split_inv
    result = []
    i, j = 0, 0
    len_input = len(left) + len(right)
    len_left = len(left)

    while i < len_left and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            split_inv += len_left - i

    result += left[i:]
    result += right[j:]

    return result

def mergesort(array):
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    left = mergesort(array[:middle])
    right = mergesort(array[middle:])

    return merge(left, right)

input_array = []

with open('Hash.txt', 'r') as f:
    for line in f:
        input_array.append(int(line.rstrip()))

print "data loaded"

A = mergesort(input_array)

del input_array

print "data sorted"

Tees = dict()

for i in xrange(-10000, 10001):
    Tees[i] = 0


for x in A:
    lower_bound = -10000 - x
    upper_bound = 10000 - x

    left = bisect.bisect_left(A, lower_bound)
    right = bisect.bisect_right(A, upper_bound)

    for y in xrange(left, right):
        if x == A[y]:
            continue

        t = x + A[y]

        Tees[t] = 1
        
print sum(Tees.itervalues())