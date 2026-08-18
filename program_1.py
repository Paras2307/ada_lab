def search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def myPow(x, n):
    if n == 0:
        return 1

    if n < 0:
        return 1 / myPow(x, -n)

    half = myPow(x, n // 2)

    if n % 2 == 0:
        return half * half
    else:
        return half * half * x


# User input
nums = [int(x) for x in input("Enter sorted numbers: ").split()]
target = int(input("Enter target: "))

x = float(input("Enter base: "))
n = int(input("Enter exponent: "))

print("Index:", search(nums, target))
print("Power:", myPow(x, n))