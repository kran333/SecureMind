# def remove_duplicates(input_list):
#     try:
#         for ind in range(len(input_list)):
#             if input_list[ind] == input_list[ind + 1]:
#                 input_list.pop(ind + 1)
#     except:
#         pass
#     return input_list


def remove_duplicates(input_list):
    for main_ind in range(len(input_list)):
        sub_ind = main_ind + 1
        # print(f"Length of the list = {len(input_list)}")
        # print(f"index + 1 = {index + 1}")
        # for sub_ind in range(main_ind + 1, len(input_list)-1):
        while sub_ind < len(input_list):
            # print(f"j value = {j}")
            if input_list[main_ind] == input_list[sub_ind]:
                input_list.pop(sub_ind)
            else:
                sub_ind += 1
    return input_list


in_lis = ['be', 'be', 'is', 'not', 'or', 'question', 'that', 'the', 'to', 'to']
in_lis2 = ['duplicate', 'duplicate', 'duplicate', 'duplicate', 'duplicate']
in_lis3 = ['be', 'is', 'not', 'or', 'question', 'that', 'the', 'to']

opt = remove_duplicates(in_lis3)
print(opt)
