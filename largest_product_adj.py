arr = list(map(int, input("Enter numbers separated by space: ").split()))
x= -10**3
for i in range(len(arr)-1):
    x= max(x, arr[i] * arr[i+1])
print("Largest product of adjacent elements:", x)
