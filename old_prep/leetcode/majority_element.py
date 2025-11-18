nums = [2,2,1,1,1,2,2]

def majorityElement(nums):
    element = {}
    for i in range(0,len(nums)):
        if nums[i] in element:
            element[nums[i]] += 1
        else:
            element[nums[i]] = 1

    n = len(nums)
    for key, value in element.items():
        if value > n//2:
            return key
    
print(majorityElement(nums))