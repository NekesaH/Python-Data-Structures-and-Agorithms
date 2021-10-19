def duplicateZeros(nums):
    nums = [1,3,0,5]
    for i in nums:
        if i == 0:
            nums.insert(i+1, 0)

    print(nums)


