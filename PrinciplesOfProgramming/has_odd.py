def has_odd(input_set):
    if len(input_set) == 0:
        return False
    opt = False
    for element in input_set:
        if element % 2 == 1:
            opt = True
    return opt


list1 = {112, 10, 4, 6, 8}
print(has_odd(list1))