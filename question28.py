n = int(input("Enter a number: "))
original = n
total = 0
digits = len(str(n))

while n > 0:
    digit = n % 10
    total = total + digit ** digits
    n = n // 10

if original >= 0 and total == original:
    print("Armstrong number")
else:
    print("Not an Armstrong number")