def read_file_data(file_name):
    f = open(file_name, 'r')
    input_data = f.read()
    f.close()
    return input_data