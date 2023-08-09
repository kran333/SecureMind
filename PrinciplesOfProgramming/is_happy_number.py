"""
Write a function named is_happy_number that returns whether a given integer is "happy".
An integer is "happy" if repeatedly summing the squares of its digits eventually leads to the number 1.

For example, 139 is happy because:

12 + 32 + 92 = 91
92 + 12 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
By contrast, 4 is not happy because:

42 = 16
12 + 62 = 37
32 + 72 = 58
52 + 82 = 89
82 + 92 = 145
12 + 42 + 52 = 42
42 + 22 = 20
22 + 02 = 4
...
"""
def is_happy_number(input_num):
    opt_res = False
    itr_count = 0
    while input_num != 1:
        dig_sum = 0
        if itr_count == 100:
            return opt_res
        while input_num > 0:
            dig_sum += (input_num % 10) * (input_num % 10)
            input_num = input_num // 10
        input_num = dig_sum
        itr_count += 1
    if input_num == 1:
        opt_res = True
    return opt_res



print(is_happy_number(31))