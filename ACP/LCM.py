# Program to find LCM of two numbers

# Take input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Find greater number
if num1 > num2:
    greater = num1
else:
    greater = num2

# Find LCM
while True:
    if greater % num1 == 0 and greater % num2 == 0:
        lcm = greater
        break
    greater += 1

# Display result
print("LCM of", num1, "and", num2, "is:", lcm)