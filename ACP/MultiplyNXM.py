# Program to multiply N to M using 2 functions

# Function with 1 iteration
def multiply_one_iteration(n, m):
    return n * m


# Function using N iterations
def multiply_n_iterations(n, m):
    result = 0

    for i in range(n):
        result = result + m

    return result


# Taking input from user
N = int(input("Enter value of N: "))
M = int(input("Enter value of M: "))

# Calling functions
print("Multiplication using 1 iteration =", multiply_one_iteration(N, M))
print("Multiplication using N iterations =", multiply_n_iterations(N, M))