import mymath
import math
# Example usage of mymath (if available)
# print("Addition:", mymath.add(10, 15))
# print("Subtraction:", mymath.subtract(10, 5))

# 1. Square root of 625
print("Square root of 625:", math.sqrt(625))

# 2. Factorial of 6
print("Factorial of 6:", math.factorial(6))

# 3. Floor and ceiling values of 4.7
print("Floor of 4.7:", math.floor(4.7))
print("Ceiling of 4.7:", math.ceil(4.7))

# 4. 5 raised to the power 3
print("5 raised to the power 3:", math.pow(5, 3))

# 5. Absolute value of -18 using math.fabs()
print("Absolute value of -18:", math.fabs(-18))

# 6. Sine, cosine, and tangent of 90 degrees
angle_deg = 90
angle_rad = math.radians(angle_deg)
print(f"Sine of {angle_deg} degrees:", math.sin(angle_rad))
print(f"Cosine of {angle_deg} degrees:", math.cos(angle_rad))
print(f"Tangent of {angle_deg} degrees:", math.tan(angle_rad))

# 7. GCD of 36 and 60
print("GCD of 36 and 60:", math.gcd(36, 60))

def add(a, b):
    return a + b

def subtract(a, b): 
    return a - b

print("Addition", add(10, 15))
print("Subtraction", subtract(10, 5))
print("Multiplication", mymath.multiply(10, 5))
print("Division", mymath.divide(10, 5))
print("square",mymath.square )

