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