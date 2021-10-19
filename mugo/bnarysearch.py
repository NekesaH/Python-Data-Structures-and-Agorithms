def binary_search(sequence, item):
    start = 0
    end = len(sequence) -1
    while start <= end:
        mid = start + (end-start)//2
        mid_value = sequence[mid]
        if mid_value == item:
            return mid

        elif item < mid_value:
            end = mid -1

        else:
            start = mid + 1

    return None


if __name__ == "__main__":
    sequence= [2, 3, 4, 10, 15, 17, 20, 23, 27, 30]
    item = 23
    result = binary_search(sequence, item)
    if result != None:
        print(sequence[result])


        
