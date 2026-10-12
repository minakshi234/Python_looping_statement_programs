n = int(input("Enter a number: "))
original = n
total = 0

while n > 0:
    digit = n % 10
    fact = 1

    for i in range(1, digit + 1):
        fact = fact * i

    total = total + fact
    n = n // 10

if original >= 0 and total == original:
    print("Strong number")
else:
    print("Not a Strong number")