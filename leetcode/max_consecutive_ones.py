nums = [1, 1, 0, 1, 1, 1]

def find_max_consecutive_ones(nums):
    max_count = 0
    current_count = 0
    for number in nums:
        if number == 1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count

print(find_max_consecutive_ones(nums))