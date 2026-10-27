def findMinMax(nums):
    if len(nums) == 1:
        return nums[0], nums[0]

    if len(nums) == 2:
        return min(nums), max(nums)

    mid = len(nums) // 2

    min1, max1 = findMinMax(nums[:mid])
    min2, max2 = findMinMax(nums[mid:])

    return min(min1, min2), max(max1, max2)
nums = [4, 2, 8, 1, 6, 3]
minimum, maximum = findMinMax(nums)
print("Minimum:", minimum)
print("Maximum:", maximum)