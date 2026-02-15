def factorial(n):
    if n==1:
        return 1
    fact = n * factorial(n-1)
    return fact

number = int(input("Enter a number : "))
result = factorial(number)
print(f"Factorial of {number} is {result}")