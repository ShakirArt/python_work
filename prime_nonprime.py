arr = list(map(int, input("Enter numbers separated by space: ").split()))
prime = []
non_prime = []

for num in arr:
    if num < 2:
        non_prime.append(num)
    else:
        for i in range(2, num):
            if num % i == 0:
                non_prime.append(num)
                break
        else:
            prime.append(num)

print("Prime numbers:", prime)
print("Non-prime numbers:", non_prime)