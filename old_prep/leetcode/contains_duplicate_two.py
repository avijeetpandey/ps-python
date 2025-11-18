def containsNearbyDuplicate(nums, k):
    last_seen = {}
    for i in range(len(nums)):
        if nums[i] in last_seen:
            previous_index = last_seen[nums[i]]
            if abs(previous_index - i) <= k:
                return True
        last_seen[nums[i]] = i
    return False
