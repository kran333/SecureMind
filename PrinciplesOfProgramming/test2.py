def is_special(interesting_int):
    factor = 2
    while interesting_int % factor != 0:
        factor += 1

    return (factor == interesting_int) or (interesting_int == 42)


res = is_special(91)
print(res)