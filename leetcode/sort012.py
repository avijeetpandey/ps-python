nums = [0, 1, 2, 0, 1, 2]

def sort012(nums):
    zero_count = 0
    one_count = 0
    two_count = 0

    for number in nums:
        if number == 0:
            zero_count += 1
        elif number == 1:
            one_count += 1
        else:
            two_count += 1

    # Reconstruct the array
    position = 0
    for i in range(zero_count):
        nums[position] = 0
        position += 1
    for i in range(one_count):
        nums[position] = 1
        position += 1
    for i in range(two_count):
        nums[position] = 2
        position += 1


sort012(nums)

print(nums)