# Method 1: Direct multiplication (1 iteration / O(1))
def multiply_direct(n, m):
    return n * m


# Method 2: Repeated addition (N iterations / O(n))
def multiply_iterative(n, m):
    result = 0
    for i in range(n):   # run loop n times
        result += m
    return result