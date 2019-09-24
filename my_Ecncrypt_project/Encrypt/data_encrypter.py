import hashlib
def encrypt_data(in_data,split_index_list):
    stage1_enc_dict = {}
    no_of_parts = len(split_index_list)
    count = 1
    for x in range(len(split_index_list)):
        if count <= no_of_parts:
            try:
                enc_data = hashlib.md5(in_data[split_index_list[x]:split_index_list[x+1]].encode())
            except IndexError:
                enc_data = hashlib.md5(in_data[split_index_list[x]:len(in_data)].encode())
            enc_data = enc_data.hexdigest()
            stage1_enc_dict[count]=enc_data
            count += 1
    return stage1_enc_dict