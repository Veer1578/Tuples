def palindrome(p):
    e = len(p) - 1
    s = 0
    while s < e:
        if(p[s] != p[e]):
            return False
        s += 1
        e -= 1
    return True

p = (1, 2, 3, 3, 2, 1)

if palindrome(p):
    print('The tuple is flip-flop')
else:
    print('The tuple is not flip-flop')