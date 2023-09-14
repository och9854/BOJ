while 1:
    a, b = map(int, input().split())
    # stop
    if a == 0:
        break
    # check
    if b % a == 0:
        print('factor')
    else:
        print('multiple' if a % b == 0 else 'neither')
