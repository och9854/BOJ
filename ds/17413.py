import re
for i in list(filter(None, re.split('(<[\d\w\s]*>|\s)', input()))):
    print(i[::-1]if i[0] != '<'else i, end='')
