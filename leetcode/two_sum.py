# given array and target number return indices of the two numbers such that they add up to target

def two_sum(nums, target):
    number_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in number_map:
            return [number_map[complement], index]
        number_map[num] = index
    return []

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)

print(result)