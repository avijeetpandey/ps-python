brands = ['Toyota', 'BMW', 'Skoda', 'Maruti', 'Suzuki']

# iterating over the brands
for i in range(len(brands)):
    print(brands[i])

# for in range
for brand in brands:
    print(brand)

# list comprehension
## list comprehension is a way to create a list quickly
ten_numbers = [x for x in range(10)]
print(ten_numbers)

## create a list of cube numbers using list comprehension
cube_numbers = [x**3 for x in range(10)]
print(cube_numbers)

## create a static list of numbers using list comprehension
static_numbers = [5]*10
print(static_numbers)

## create a 2d list using list comprehension
two_d_list = [(i,j) for i in range(5) for j in range(4)]
print(two_d_list)

## slicing the list
print(ten_numbers[0:5])  # prints first 5 elements
print(cube_numbers[5:])   # prints elements from index 5 to end
print(static_numbers[:3])  # prints first 3 elements
print(two_d_list[1:3])     # prints 2d list from index 1 to 2

numbers_set = set()
numbers = [1,1,1,4,5,6,6,9,9,9,0,1]

total_duplicates = 0

for number in numbers:
    if number in numbers_set:
        total_duplicates += 1
    else:
        numbers_set.add(number)