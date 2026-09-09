# Sum of three digit numbers without loops.

# Take inputs
input_num = input("Enter 3 digit number: ")

# Get the length
length = len(input_num)

# Convert to int
num = int(input_num)

# Only three digits allowed
if length == 3:
    a = num % 10
    num = num // 10
    b = num % 10
    num = num // 10
    c = num % 10

    print(a+b+c)
else:
    print("Please enter 3 digits!")