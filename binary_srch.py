a=(2, 5, 8, 12, 16, 23, 38, 56, 72, 91)

x= int(input("Enter a number to search: "))

low=0
high=len(a)-1

while low <= high:
    mid = (low + high) // 2
    if a[mid] == x:
        print(f"Number found at index {mid}")
        break
    elif a[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Number not found")