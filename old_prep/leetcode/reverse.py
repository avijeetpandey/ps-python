nums = [1,2,3,4,5]

def reverse(nums, start, end):
    i = start
    j = end

    while i < j:
        nums[i], nums[j] = nums[j] , nums[i]
        i += 1
        j -= 1
