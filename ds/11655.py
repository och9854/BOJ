# rot 13
# B1
# abcde fghij klmno pqrst uvwxy z
# nopqr stuvw xyzab cdefg hijkl m
s = input()
ans = ''
for i in s:
    # change
    if i.isdigit() or i == " ":  # space or num
        ans += i
    elif i.islower():  # lower
        pos = ord(i)+13 if ord(i)+13 <= ord('z') else ord(i)-13
        ans += chr(pos)
    elif i.isupper():          # upper
        pos = ord(i)+13 if ord(i)+13 <= ord('Z') else ord(i)-13
        ans += chr(pos)

    # add to ans

print(ans)
