n = int(input("Enter a number: "))
count = 0

for i in range(1, n + 1):
    if n > 1 and n % i == 0:
        count = count + 1

if count == 2:
    print("Prime number")
else:
    print("Not a prime number")