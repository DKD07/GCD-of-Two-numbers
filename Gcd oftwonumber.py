def gcd(a, b):
    # Base case: when b is 0, the GCD is a
    if b == 0:
        return a
    else:
        # Recursive case: compute the GCD using the Euclidean algorithm
        return gcd(b, a % b)

# Example usage
num1 = int(input("Enter the value of num1: "))
num2 = int(input("Enter the value of num2: "))
result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {result}")

 