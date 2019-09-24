def enc_data_write_function(file_name,data):
    file_name = 'encrypted_'+file_name
    f = open(file_name,'w')
    f.write(data)
    f.close()