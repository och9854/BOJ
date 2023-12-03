n, k = map(int, input().split())
factors = [i for i in range(1, n+1) if n % i == 0]
print(factors[k-1] if len(factors) >= k else 0)
