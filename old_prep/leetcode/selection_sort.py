numbers = [3, 9, 0, 12, -11, 6, 3]

def selectionSort(nums):
    for i in range(len(nums)):
        smallNumberIndex = i
        for j in range(i,len(nums)):
            if nums[j] < nums[smallNumberIndex]:
                smallNumberIndex = j
        nums[i], nums[smallNumberIndex] = nums[smallNumberIndex], nums[i]

selectionSort(numbers)

print(numbers)