### File 1: Introduction to Python

# Printing Statements
# Definition: Printing statements display output to the console.
print("Hello World")  # Using double quotes
print('Hello World')  # Using single quotes

# Variables and User Input
# Definition: Variables store data, and input allows users to provide data during program execution.
greet = "Welcome user!"
name = input("What is your name? ")  # Stores the user's name
age = input("What is your age? ")  # Stores the user's age
isGenius = input("Are you genius? ")  # Stores a boolean-like response

print(name, age, isGenius)

# Type Conversion
# Definition: Converts data from one type to another.
new_age = int(age) + 1  # Converts age to integer and increments it by 1

# Built-in Functions for Type Conversion
str()   # Converts value to string
float() # Converts value to float
bool()  # Converts value to boolean

# Displaying Information Using Concatenation
print("Hello " + name, age, isGenius)

# Comments
# Definition: Comments are notes in the code that are not executed.
# Use the '#' symbol for single-line comments

# Example of Addition Using Input
a = input("Enter a: ")
b = input("Enter b: ")
sum = int(a) + int(b)
print(sum)