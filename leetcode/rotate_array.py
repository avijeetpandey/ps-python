nums = [1, 2, 3, 5, 6, 7]


def reverse(nums, start, end):
    i = start
    j = end
    while i < j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1


def rotateArray(nums, k):
    n = len(nums)
    k = k % n
    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)


rotateArray(nums, 3)
print(nums)
