text = input("Enter a string: ")

reverse = text[::-1]

if text == reverse:
    print("Palindrome string")
else:
    print("Not a palindrome string")