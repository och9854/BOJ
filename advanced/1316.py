n = int(input())
word_list = [input() for i in range(n)]
result = 0

# check


def check(word):
    if len(word) == 1:
        return True
    else:
        passed = ""
        for idx, char in enumerate(word):  # each character
            if char not in passed:
                passed += char
                continue
            elif idx >= 1:
                if word[idx-1] != char:
                    return 0
                else:
                    continue
        return 1


for word in word_list:
    result += check(word)

print(result)

# Short code
'''
result = 0
for i in range(int(input())):
    word = input()
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)
'''
