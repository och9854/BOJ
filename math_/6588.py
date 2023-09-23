# s1

# try1: wrong - timeout
'''

def check_prime(num):
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            return 0
            break
    else:
        return 1


def check(n):
    for i in range(3, int(n/2)+1, 2):  # travers from 2 to (n-1)/2 ++2
        # if found:

        #check prime(i) -> if it's prime -> check prime(n - i)  -> print() if yes else continue

        if check_prime(i):
            if check_prime(n-i):
                return f"{n} = {i} + {n-i}"
            else:
                continue
    return "Goldbach's conjecture is wrong."


while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        print(check(n))
'''

# try2:
# refer: https://velog.io/@cjkangme/%EB%B0%B1%EC%A4%80-6588.-%EA%B3%A8%EB%93%9C%EB%B0%94%ED%9D%90%EC%9D%98-%EC%B6%94%EC%B8%A1-%ED%8C%8C%EC%9D%B4%EC%8D%AC
'''
    find all of the list{odd prime nums} when n is 6<= n <= 1,000.000
    check test case is in the list
        if yes: print(i, num- i)
        else: print("wrong")
'''
# find all the list
import sys
MAX_NUM = 1000001
prime_list = [False] * 2 + [True] * (MAX_NUM-2)
for i in range(3, int(MAX_NUM**0.5), 2):
    if prime_list[i]:
        # assign to each multiples
        prime_list[i+i::i] = [0] * ((MAX_NUM-i-1)//i)

# 소수 리스트 구하기
prime = []
for i in range(3, MAX_NUM, 2):
    if prime_list[i]:
        prime.append(i)

# check the test case if it's in the list
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    # TRAVERSE prime
    for i in prime:
        if prime_list[n-i]:
            print("%d = %d + %d" % (n, i, n-i))
            break
