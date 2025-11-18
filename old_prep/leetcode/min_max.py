nums = [5, 2, 8, 1, 9]


def findMinMax(nums):
    if not nums:
        return None, None
    min_value = nums[0]
    max_value = nums[0]

    for number in nums[1:]:
        if number < min_value:
            min_value = number
        elif number > max_value:
            max_value = number

    return min_value, max_value

print(findMinMax(nums))
