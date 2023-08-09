import random
import pandas as pd

class CommonRnCt:
    def __init__(self):
        self.__hexa_chars = "0123456789ABCDEF"
        self.__crypt_table = []
    def get_random_number(self, bit_size):
        __rand_number = 0
        while __rand_number.bit_length() != bit_size:
            __rand_number = random.getrandbits(bit_size)
        return __rand_number

    def crypto_table(self, size):
        for x in range(size):
            __temp_list = []
            for y in range(size):
                __temp_list.append(random.choice(self.__hexa_chars))
            self.__crypt_table.append(__temp_list)
        return pd.DataFrame(self.__crypt_table)