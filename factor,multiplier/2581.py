n = int(input())
m = int(input())
nums = [i for i in range(n, m+1)]
primes = []

for num in nums:
    for i in range(2, num+1):
        if i == num:
            primes.append(num)
        elif num % i == 0:
            break

print(-1) if len(primes) == 0 else print(f"{sum(primes)}\n{primes[0]}")
