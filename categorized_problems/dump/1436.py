n = int(input())
cnt = 1
end_list = [666]
num = 666
while cnt <= n:
    if '666' in str(num):  # 연속으로
        end_list.append(num)
        cnt += 1
    num += 1

print(end_list[-1])
