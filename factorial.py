def fact1(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(fact1(5))