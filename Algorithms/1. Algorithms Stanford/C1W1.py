# Karatsuba multiplication
'''
import time
start_time = time.time()

def karatsuba(x,y):
    if len(str(x)) or len(str(y)):
        return x*y

    m = max(len(str(x)), len(str(y)))#calculate the size of number
    
    num1 = str(x)
    num2 = str(y)
    a,b = num1[:len(num1)/2], num1[len(num1)/2:]
    c,d = num2[:len(num2)/2], num2[len(num2)/2:]
    (a,b) = map(int,(a,b))
    (c,d) = map(int,(c,d))
 
    z0 = karatsuba(b,d)
    z1 = karatsuba((b+a),(d+c))
    z2 = karatsuba(a,c)
    return (z2*(10**(m))) + ((z1-z2-z0)*(10**(m/2))) + (z0)

answer = karatsuba(453,763)
print answer

end_time = time.time()
print end_time - start_time, "seconds"
'''


#Merge sort algorithm
'''
import timeit
start_time = timeit.timeit()

def insertion_sort(alist):
    for index in range(1, len(alist)):
        current_value = alist[index]
        position = index        
        while position > 0 and alist[position-1] > current_value:
            alist[position] = alist[position-1]
            position = position - 1
        alist[position] = current_value

def merge_sort(alist):
    if len(alist)>1:
        L_lst = alist[:len(alist)/2]
        R_lst = alist[len(alist)/2:]      
        merge_sort(L_lst)
        merge_sort(R_lst)        
        i = 0
        j = 0
        k = 0        
        while i<len(L_lst) and j<len(R_lst):
            if L_lst[i] < R_lst[j]:
                alist[k] = L_lst[i]
                i+=1
            else:
                alist[k] = R_lst[j]
                j+=1
            k+=1
        while i<len(L_lst):
            alist[k] = L_lst[i]
            i+=1
            k+=1
        while j<len(R_lst):
            alist[k] = R_lst[j]
            j+=1
            k+=1
    return (alist)       
        
lst = []
   
if len(lst)>0 and len(lst)<90: #perform insertion sort       
    insertion_sort(lst)
    print "Insertion sort Complete\nSorted list:%s" %(lst)
    
if len(lst)>90: #perform merge & sort
    merge_sort(lst)  
    print "Merge & sort Complete\nSorted list:%s" %(lst)

end_time = timeit.timeit()
print "run time= ",end_time - start_time, "seconds"
'''

#Merge_Insertion_Sort
#'''
import timeit
start_time = timeit.timeit()

def Merge_Insertion_Sort(alist):




end_time = timeit.timeit()
print "run time= ",end_time - start_time, "seconds"
#'''