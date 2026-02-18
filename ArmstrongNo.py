#Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

num = int(input("Enter a number: "))

temp = num
digits = len(str(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digits
    temp //= 10

if sum == num:
    print(num, "is an Armstrong Number")
else:
    print(num, "is NOT an Armstrong Number")
