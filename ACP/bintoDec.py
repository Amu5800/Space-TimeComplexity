# Program to convert Binary number to Decimal number

# Take binary number as input
binary = input("Enter a binary number: ")

# Initialize variables
decimal = 0
power = 0

# Traverse binary number from right to left
for digit in reversed(binary):

    if digit == '1':
        decimal = decimal + (2 ** power)

    power = power + 1

# Display result
print("Decimal number is:", decimal)