def switch_pairs(input_list):
    copy_list = input_list
    in_lis_len = len(input_list)
    if in_lis_len % 2 == 1:
        in_lis_len = in_lis_len - 1
    for x in range(0,in_lis_len):
        if x % 2 == 0:
            copy_list[x], copy_list[x+1] = input_list[x+1], input_list[x]
    return copy_list

in_lis = ['a', 'bb', 'c', 'ddd', 'f', 'ee']
opt = switch_pairs(in_lis)
print(opt)