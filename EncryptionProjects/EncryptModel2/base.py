import random
import pandas as pd

def get_random_number(bit_size):
    rand_num = 0
    while rand_num.bit_length() != bit_size:
        rand_num = random.getrandbits(bit_size)
    return rand_num

# Crypto Table generation
def get_crypt_tbl(size):
    hexa_val = "0123456789ABCDEF"
    crypt_table = []
    for _ in range(size):
        temp_list = []
        for _ in range(size):
            temp_list.append(random.choice(hexa_val))
        crypt_table.append(temp_list)
    return pd.DataFrame(crypt_table)


RN = get_random_number(256)
PWD = get_random_number(6)
CT = get_crypt_tbl(32)