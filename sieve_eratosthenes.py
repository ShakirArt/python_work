start = int(input("Enter 1st number: "))
end = int(input("Enter last number: "))

arr = [1] * (end + 1)
arr[0], arr[1] = 0, 0

i = 2
while i * i <= end:  
    if arr[i] == 1:
        for j in range(i * i, end + 1, i):
            arr[j] = 0
    i += 1

print("Prime numbers between", start, "and", end, "are:")
for i in range(start, end + 1):
    if arr[i] == 1:
        print(i, end=" ")
print()

