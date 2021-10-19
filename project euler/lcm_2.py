# two numbers

def lcm(num1, num2):
    if num1 > num2:
        num1, num2 = num2, num1
    for x in range(num2 , num1 * num2 + 1, num2):
        if x % num1 == 0:
            return x

def lcm3(nums):
    nums.sort()
    worst = nums[0] * nums[1] * nums[2]

    for x in range(nums[2], worst + 1, nums[2]):
        if x % nums[0] == 0 and x % nums[1] == 0:
            return x
