# def min_to_front(input_list):
#     out_list = []
#     min_num_ind = 0
#     for x in range(0, input_list):
#         if input_list[x] < min_num:
#             min_num = x
#     out_list.append(min_num)
#     for x in input_list:
#         if x not in out_list:
#             out_list.append(x)
#     return out_list


def min_to_front(input_list):
    input_list.insert(0, input_list.pop(input_list.index(min(input_list))))
    return input_list


in_lis = [3, 8, 92, 4, 2, 17, 9]

opt = min_to_front(in_lis)
print(opt)