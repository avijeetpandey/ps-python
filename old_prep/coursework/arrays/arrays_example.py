'''
Python provides list data structure to store contigious data, underlying implementation of python list
is a dynamic resizable array.
'''

brands = ['Toyota', 'Toyota', 'Honda', 'Ford', 'Tesla']

# length of the array
print(len(brands))

# appending in an array
brands.append('BMW')
print(brands)

# removing the last element from the array
brands.pop()
print(brands)

# counting the ocuurences of an element
print(brands.count('Toyota'))

numbers = [1, 45, 89, -109, 0, 68]

# sorting the numbers
numbers.sort()
print(numbers)

# reverse sort the numbers
numbers.sort(reverse=True)
print(numbers)