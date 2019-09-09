import hashlib
import random
import re

f_name = 'data.txt'
def read_file_data(file_name):
    f = open(file_name, 'r')
    input_data = f.read()
    return input_data

input_data = read_file_data(f_name)
input_data_length = len(read_file_data(f_name))


def split_data_function(input_data_length,no_of_splits):
    split_index = []
    temp = 0
    num = input_data_length % no_of_splits
    size = int(input_data_length/no_of_splits)
    while temp < (input_data_length-num):
        split_index.append(temp)
        temp = temp + size
    return split_index

split_size = split_data_function(input_data_length,5)

def encrypt_data_stage_1(in_data,split_index_list):
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
print encrypt_data_stage_1(input_data,split_size)

def add_salt(salt_list):
    defult_salt =["$$$","%%%","&&&",'***','###','^^^']
    for x in defult_salt:
        salt_list.append(x)
    enc_salt = {}
    for x in salt_list:
        enc_salt[x] = hashlib.sha1(x).hexdigest()
    return random.choice(enc_salt.values())

print add_salt(['^%&'])

# encrypted_data_stage_1 = enc_data_part_1 + random.choice(enc_salt.values()) + enc_data_part_2
# encrypted_data_stage_2 = hashlib.sha224(encrypted_data_stage_1.encode())
# encrypted_data_stage_2 = encrypted_data_stage_2.hexdigest()
# final_enctypted_data = hashlib.sha512(encrypted_data_stage_2.encode())
# final_enctypted_data = final_enctypted_data.hexdigest()
# print final_enctypted_data



