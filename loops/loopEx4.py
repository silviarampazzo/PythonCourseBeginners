def factorial(x):
    prod = 1
    while x >= 1:
        prod *= x
        x -= 1
    return prod


print((factorial(3)))
print((factorial(4)))
print((factorial(5)))
