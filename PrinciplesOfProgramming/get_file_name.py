import os
def get_file_name():
    input_file = ''
    while not os.path.isfile(input_file):
        input_file = input("Type a file name: ")
    return input_file

print(get_file_name())