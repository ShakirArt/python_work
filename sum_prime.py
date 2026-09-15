val = list(map(int, input("Enter numbers separated by space: ").split()))

total = sum(val)

if total < 2:
    print(total, "is not prime")
else:
    for i in range(2, total):
        if total % i == 0:
            print(total, "is not prime")
            break
    else:
        print(total, "is prime")
