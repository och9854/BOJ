score = []
grade = []
product_sum = 0
score_list = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F":    0,
}
cnt = 0
for _ in range(20):

    _, a, b = input().split()
    if b == 'P':
        continue
    cnt += 1 * float(a)
    product_sum += float(a) * score_list[b]


print(product_sum / cnt)
