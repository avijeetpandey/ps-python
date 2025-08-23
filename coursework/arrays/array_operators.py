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