#merge sort algorithms
#Time complexity
# Space Complexity
# Time = O(N log(N)) Space = O(N log(N))

#from heapq import merge



def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
  
    #recursion
    
    merge_sort(left_arr)
    merge_sort(right_arr)

    i=0 # left_array index
    j=0 #right_array index
    k = 0 #merged array index

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
            
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1 

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1


arr_test = [2, 3, 5, 1,7, 4, 4, 4, 2, 6, 0]
merge_sort(arr_test)
print(arr_test)







#insertion sort
# space O(1)
# Time 0(n2)

# def insertion_sort(array):
#     i = j
#     for i in range(1, len(array)):
#         while j > 0 and array[j] < array[j-1]:
#             swap(i, j-1, array)
#             j -= 1

# def swap(array, i , j):
#     array[i], array[j] = array[j], array[i]


        




































































