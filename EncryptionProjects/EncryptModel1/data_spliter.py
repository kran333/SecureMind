def split_data_function(input_data_length,no_of_splits=3):
    split_index = []
    temp = 0
    num = input_data_length % no_of_splits
    size = int(input_data_length/no_of_splits)
    while temp < (input_data_length-num):
        split_index.append(temp)
        temp = temp + size
    return split_index