a = input("Enter a word or number: ")

if a == a[::-1]:
    print("The word or number is a palindrome")
else:
    print("The word or number is not a palindrome")
