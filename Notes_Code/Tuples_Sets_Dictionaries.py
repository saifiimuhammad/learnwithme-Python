### File 4: Tuples, Sets, and Dictionaries

# Tuples
# Definition: Tuples are immutable collections of items.
marks = (44, 55, 44, 44, 33, 33)
marks = 44, 55, 44, 44, 33, 33 # Also a tuple
print(marks.count(44))
print(marks.index(55))

# Sets
# Definition: Sets store unique, unordered items.
marks = {'Saif', 'Sarim', 'Afandi', 'Haris', 'Umer', 'Saif'}
print(marks) # prints all values once
for mark in marks:
    print(mark)

# Dictionaries
# Definition: Dictionaries store key-value pairs.
marks = {'Saif': 44, 'Sarim': 55, 'Afandi': 44, 'Haris': 44, 'Umer': 33}
print(marks['Saif'])
marks['Haroon'] = 67
print(marks)