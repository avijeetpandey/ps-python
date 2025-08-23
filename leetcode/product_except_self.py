numbers = [1,2,3,4]

def productExceptSelf(numbers):
    product = 1
    for number in numbers:
        product *= number

    output_array = []
    for number in numbers:
        output_array.append(product // number)
    
    return output_array

print(productExceptSelf(numbers))


def productExceptSelfOptimised(numbers):
    n = len(numbers)
    left = [1] * n
    right = [1] * n

    for i in range(1, n):
        left[i] = left[i-1] * numbers[i-1]

    for i in range(n-2, -1, -1):
        right[i] = right[i+1] * numbers[i+1]

    output = []
    for i in range(n):
        output.append(left[i]*right[i])
    
    return output

print(productExceptSelfOptimised(numbers))