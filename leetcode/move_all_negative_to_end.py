nums = [1, -1, 3, 2, -7, -5, 11, 6]

# move all the elements to the end in place


def moveAllNegativeToEnd(nums):
    positive_elements = []
    negative_elements = []

    for number in nums:
        if number < 0:
            negative_elements.append(number)
        else:
            positive_elements.append(number)

    # putting all the numbers together
    position = 0
    for i in range(len(positive_elements)):
        nums[position] = positive_elements[i]
        position += 1

    for i in range(len(negative_elements)):
        nums[position] = negative_elements[i]
        position += 1
