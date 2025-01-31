### File 3: Loops and Lists

# Loops
# Definition: Execute a block of code multiple times.

# Using Range in Loops
print(range(5))  # Range Object

# While Loop Example
i = 1
while i <= 5:
    print(i * '*')
    i += 1

# Reverse Triangle
i = 5
while i >= 1:
    print(i * '*')
    i -= 1

# For Loop Example
for i in range(10):
    print(i * '*')

# Lists
# Definition: Lists store ordered collections of items.
friends = ['Saif', 'Sarim', 'Abdullah']

# Iterating Through a List
for friend in friends:
    print(friend)

# Accessing List Elements
print(friends[-2])
print(friends[1:])
print(friends[1:3])

# List Functions
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends.extend(lucky_numbers)  # Extends the List
print(friends)

friends.append('Sarim')  # Appends an Element
print(friends)

# Insert at Specific Index
marks = [50, 60, 70]
marks.insert(0, 80)
for score in marks:
    print(score)

# Check if an Element Exists in the List
print(80 in marks)

# Get the Length of the List
print(len(marks))

# Iterate Using While Loop
i = 0
while i < len(marks):
    print(marks[i])
    i += 1

# Using Break and Continue
students = ['Saif', 'Sarim', 'Abdullah', 'Afandi', 'Haroon', 'Haris']
for student in students:
    if student == 'Haroon':
        break
    elif student == 'Sarim':
        continue
    print(student)