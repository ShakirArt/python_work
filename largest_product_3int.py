arr = list(map(int, input("Enter numbers separated by space: ").split()))
arr.sort()
x= max(arr[-1] * arr[-2] * arr[-3], arr[0] * arr[1] * arr[-1])
print(x)
