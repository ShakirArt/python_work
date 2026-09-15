start = int(input("Enter 1st number: "))
end = int(input("Enter last number: "))
arr = []

for i in range(start, end + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            arr.append(i)

print("Prime numbers between", start, "and", end, "are:", arr)
