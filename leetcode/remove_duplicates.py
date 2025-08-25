nums = [1, 1, 2]


def removeDuplicates(nums):
    st = set()
    for num in nums:
        st.add(num)

    return len(st)


print(removeDuplicates(nums))
