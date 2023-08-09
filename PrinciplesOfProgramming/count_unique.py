def count_unique(a, b, c):
    count = 3
    if (a == b) or (a == c):
        count = count - 1
    if (b == c):
        count = count - 1
    return count



opt = count_unique(6, 7, 6)
print(opt)
