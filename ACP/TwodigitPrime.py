# Program to print all two-digit prime numbers

print("Two-digit prime numbers are:")

for num in range(10, 100):

    # Assume number is prime
    isPrime = True

    # Check divisibility
    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break

    # Print prime number
    if isPrime:
        print(num, end=" ")