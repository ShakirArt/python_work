str1, str2 = input("Enter two strings separated by space: ").split()
if all(i in str1 for i in str2):
    print("true")
else:
    print("false")
