def bubbleSort(nums):
    n = len(nums)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swapped = True
        if not swapped:
            break
nums = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(nums)
print(nums)