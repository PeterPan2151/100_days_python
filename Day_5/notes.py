fruits = ['Apple', 'Peach', 'Pear']

# Loop items inside a list
# 'fruit' is a variable we make, for each iteration it will have a different value for each item in the list.
for fruit in fruits: 
    print(fruit)

# For loop with range(), (a, b) : a is inclusive, b is exclusive
for n in range(1, 10):
    print(n)

total = 0
for n in range(1, 101):
    total += n