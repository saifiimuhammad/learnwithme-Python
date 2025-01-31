### File 2: String Operations

# Strings
# Definition: Strings are sequences of characters used to store text.
name = "saif"

# Converts all characters to uppercase
print(name.upper())

name = "SAIF"

# Converts all characters to lowercase
print(name.lower())

name = "saif is a good boy"

# Finds the index of the first occurrence of a character or substring
print(name.find('i'))

# Replaces a Substring
print(name.replace("good", "cool"))

# Checking for Substring Presence
print("good" in name)
print("bad" in name)

# Original String Remains Unchanged
print(name)

### Arithmetic and Comparison Operators

# Arithmetic Operators
# Definition: Used to perform mathematical operations.
a = 5
b = 2
print(a // b)  # Integer Division
print(a ** b)  # Exponentiation

# Comparison Operators
# Definition: Used to compare values and return a boolean.
print(1 == 2)  # Equality
print(1 != 2)  # Inequality

# Logical Operators
# Definition: Combine multiple conditions.
print(1 == 2 and 2 == 2)  # Logical AND
print(1 == 2 or 2 == 2)   # Logical OR
print(not 5 > 3)          # Logical NOT

### Conditional Statements
# Definition: Control the flow of execution based on conditions.
age = 21

if age > 18:
    print("You are an adult")
elif age == 18:
    print("You are 18")
else:
    print("You are a child")