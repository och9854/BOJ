while 1:
    n = int(input())
    if n == -1:
        break

    factors = [i for i in range(1, n) if n % i == 0]
    if sum(factors) == n:
        print(f"{n} = ", end='')
        plus = ''.join(str(factors)).replace(
            "[", "").replace("]", "").replace(",", " +")

        print(plus)
    else:
        print(f"{n} is NOT perfect.")
