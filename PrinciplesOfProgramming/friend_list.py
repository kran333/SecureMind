def friend_list(input_file):
    output_dict = {}

    with open(input_file, 'r') as f:
        input_rd_data = f.readlines()

    for pair in input_rd_data:
        buddy = pair.split()
        if buddy[0] not in output_dict.keys():
            output_dict[buddy[0].strip()] = [buddy[1].strip()]
        else:
            if buddy[0] not in output_dict[buddy[0].strip()]:
                output_dict[buddy[0].strip()].append(buddy[1].strip())

        if buddy[1] not in output_dict.keys():
            output_dict[buddy[1].strip()] = [buddy[0].strip()]
        else:
            if buddy[1] not in output_dict[buddy[1].strip()]:
                output_dict[buddy[1].strip()].append(buddy[0].strip())
    return output_dict


res = friend_list('buddies.txt')
print(res)