


#  Error Handling

try:
    a = int(input("Enter a number: "))
    print(a)
except Exception as e:
    print("Something went wrong: ", e)


# File I/O

# Three modes of opening a file
# 1. Read mode
# 2. Write mode
# 3. Append mode


with open("file.txt", "w") as f: # auto close the file after the block
    f.write("Hello World")

# Append mode
with open("file.txt", "a") as fs:
    fs.write("Hello World 2")

# Two ways to open a file
# 1. Using open() function
# 2. Using with statement

# 1. Using open() function
f = open("file.txt", "r")
print(f.read())
f.close()

# 2. Using with statement
with open("file.txt", "r") as f:
    print(f.read())
