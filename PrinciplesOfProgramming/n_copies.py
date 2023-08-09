def n_copies(input_list):
    output_list = []
    for ele in input_list:
        for _ in range(ele):
            output_list.append(ele)
    return output_list

lis = [3, 5, 0, 2, 2, -7, 0, 4]

opt = n_copies(lis)
print(opt)