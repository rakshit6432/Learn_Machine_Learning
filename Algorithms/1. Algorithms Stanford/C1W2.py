#Closest pair Algorithm
#'''
import time
start_time = time.time()

def ():




end_time = time.time()
print "run time= ",end_time - start_time, "seconds"
#'''

#Strassens' Matrix Multiplication
#'''
import time
start_time = time.time()

def ():




end_time = time.time()
print "run time= ",end_time - start_time, "seconds"
#'''


#Counting Inversion 
'''
import time
start_time = time.time()

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count 

with open('IntegerArray.txt') as f:
    numbers = f.readlines()
numbers = [int(x.strip()) for x in numbers]
#numbers = [6, 9, 1, 14, 8, 12, 3, 2]
final = merge_count_inversion(numbers)
print final  

end_time = time.time()
print "run time= ",end_time - start_time, "seconds"
'''