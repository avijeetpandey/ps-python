nums = [1,2,3,1]

def containsDuplicate(nums):
    nums_dict = {}
    for index, number in enumerate(nums):
        if number in nums_dict:
            return True
        nums_dict[number] = index
    return False

result = containsDuplicate(nums)

print(result)