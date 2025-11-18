nums = [3,3,3,3]

def findDuplicate(nums):
    output = [False] * len(nums)

    for i in range(len(nums)):
        if output[nums[i]]:
            return nums[i]
        else:
            output[nums[i]] = True

print(findDuplicate(nums))