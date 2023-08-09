def three_consecutive(a, b, c):
    res = False
    if a+1 == b and b+1 == c:
        res = True
    if b+1 == c and c+1 == a:
        res = True
    if a+1 == c and c+1 == b:
        res = True
    if c+1 == b and b+1 == a:
        res = True
    if b+1 == a and a+1 == c:
        res = True
    return res


opt = three_consecutive(3, 2, 4)
print(opt)
