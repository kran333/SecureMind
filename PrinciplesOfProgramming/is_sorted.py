def is_sorted(num_list):
    sorted_list = []
    temp_num_list = num_list.copy()
    while temp_num_list:
        min = temp_num_list[0]
        for num in temp_num_list:
            if num < min:
                min = num
        sorted_list.append(min)
        temp_num_list.remove(min)
    if num_list ==  sorted_list:
        return True
    else:
        return False

list1 = [16.1, 12.3, 22.2, 14.4]
list2 = [1.5, 4.3, 7.0, 19.5, 25.1, 46.2]
print(is_sorted(list1))