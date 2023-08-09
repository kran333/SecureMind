import data_binder
import file_reader
import file_writer
import data_spliter
import data_encrypter
f_name = 'data.txt'
def flow_controller(file_name,no_of_stages):
    count = 1
    results = ''
    data = file_reader.read_file_data(file_name)
    temp_data = data
    data_len = len(data)
    split_indexs = data_spliter.split_data_function(data_len, 4)

    while count <= no_of_stages:
        results = data_binder.bind_data(data_encrypter.encrypt_data(temp_data, split_indexs).values())
        temp_data = results
        print results
        count = count + 1
    file_writer.enc_data_write_function(file_name, results)

flow_controller(f_name,5)




