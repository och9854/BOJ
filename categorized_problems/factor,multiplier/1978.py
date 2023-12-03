n = int(input())
nums = list(map(int, input().split()))
cnt = 0

for num in nums:
    factors = [i for i in range(2, num+1) if num % i == 0]
    cnt = cnt+1 if len(factors) == 1 else cnt

print(cnt)
# feedback
'''
- missed the definition of prime number
'''
