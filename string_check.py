str1,str2 = input("Enter two strings separated by space: ").split()
count = 0
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            count += 1
if count == len(str2):
    print("true")
else:
    print("false")